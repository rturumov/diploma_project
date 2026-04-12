from modeltranslation.translator import TranslationOptions, register

from .models import Message


@register(Message)
class MessageTranslationOptions(TranslationOptions):
    fields = ("text",)
