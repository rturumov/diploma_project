import requests
from django.core.management.base import BaseCommand
from django.conf import settings
from ai_chat.models import DocumentChunk


def get_embedding(text):
    api_url = "https://router.huggingface.co/hf-inference/models/sentence-transformers/paraphrase-multilingual-mpnet-base-v2/pipeline/feature-extraction"
    headers = {"Authorization": f"Bearer {settings.HUGGINGFACE_API_KEY}"}
    response = requests.post(api_url, headers=headers, json={"inputs": text})
    embedding = response.json()
    if isinstance(embedding[0], list):
        embedding = embedding[0]
    return embedding


class Command(BaseCommand):
    help = 'Generate embeddings for all documents'

    def handle(self, *args, **kwargs):
        docs = DocumentChunk.objects.filter(embedding__isnull=True)
        total = docs.count()
        self.stdout.write(f'Generating embeddings for {total} documents...')

        for i, doc in enumerate(docs):
            try:
                text = f"{doc.title}. {doc.content}"
                doc.embedding = get_embedding(text)
                doc.save()
                self.stdout.write(f'✓ {i+1}/{total}: {doc.title}')
            except Exception as e:
                self.stdout.write(f'✗ Error on {doc.title}: {e}')

        self.stdout.write('Done!')
