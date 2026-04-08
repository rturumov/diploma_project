import json
import requests
from groq import Groq
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from pgvector.django import CosineDistance
from .models import DocumentChunk


def get_embedding(text):
    api_url = "https://router.huggingface.co/hf-inference/models/sentence-transformers/paraphrase-multilingual-mpnet-base-v2/pipeline/feature-extraction"
    headers = {"Authorization": f"Bearer {settings.HUGGINGFACE_API_KEY}"}
    response = requests.post(api_url, headers=headers, json={"inputs": text})
    embedding = response.json()
    if isinstance(embedding[0], list):
        embedding = embedding[0]
    return embedding


def search_documents(question, top_k=5):
    try:
        question_embedding = get_embedding(question)
        results = DocumentChunk.objects.filter(
            embedding__isnull=False
        ).order_by(
            CosineDistance('embedding', question_embedding)
        )[:top_k]

        if not results:
            results = DocumentChunk.objects.filter(
                content__icontains=question
            )[:top_k]

        if not results:
            results = DocumentChunk.objects.all()[:top_k]

    except Exception:
        results = DocumentChunk.objects.filter(
            content__icontains=question
        )[:top_k]

    return results


@csrf_exempt
@require_http_methods(["POST"])
def chat(request):
    try:
        data = json.loads(request.body)
        question = data.get('question', '').strip()
        history = data.get('history', [])

        if not question:
            return JsonResponse({'error': 'Question is required'}, status=400)

        relevant_docs = search_documents(question)

        if not relevant_docs:
            context = "No documents found in the database yet."
        else:
            context = "\n\n".join([
                f"Source: {doc.source}\nTitle: {doc.title}\nContent: {doc.content}"
                for doc in relevant_docs
            ])

        messages = [
            {
                "role": "system",
                "content": f"""You are an HSE (Health, Safety, Environment) expert 
                assistant for a Kazakhstan-based platform. Answer questions based 
                ONLY on the provided documents. If the answer is not in the 
                documents, say so clearly. Always cite which document you used. 
                Respond in the same language as the question.
                
                Relevant documents:
                {context}"""
            }
        ]

        # Add chat history (last 6 messages to stay within token limits)
        for msg in history[-6:]:
            if msg['role'] in ['user', 'assistant']:
                messages.append({
                    "role": msg['role'],
                    "content": msg['content']
                })

        messages.append({"role": "user", "content": question})

        client = Groq(api_key=settings.GROQ_API_KEY)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            max_tokens=1024,
        )

        return JsonResponse({
            'answer': response.choices[0].message.content,
            'sources': [
                {'title': doc.title, 'source': doc.source}
                for doc in relevant_docs
            ]
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def chat_page(request):
    return render(request, 'ai_chat/chat.html')