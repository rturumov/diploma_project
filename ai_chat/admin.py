from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import DocumentChunk


@admin.register(DocumentChunk)
class DocumentChunkAdmin(TranslationAdmin):
    list_display = ['title', 'source', 'created_at']
    search_fields = ['title', 'content']