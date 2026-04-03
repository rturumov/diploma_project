from django.contrib import admin
from .models import DocumentChunk


@admin.register(DocumentChunk)
class DocumentChunkAdmin(admin.ModelAdmin):
    list_display = ['title', 'source', 'created_at']
    search_fields = ['title', 'content']