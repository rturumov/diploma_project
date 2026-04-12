from modeltranslation.translator import TranslationOptions, register

from .models import DocumentChunk


@register(DocumentChunk)
class DocumentChunkTranslationOptions(TranslationOptions):
    fields = ("title", "content", "source")
