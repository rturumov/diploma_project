from django.db import models
from pgvector.django import VectorField


class DocumentChunk(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    source = models.CharField(max_length=500, blank=True)
    embedding = VectorField(dimensions=768, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Document Chunk'
        verbose_name_plural = 'Document Chunks'