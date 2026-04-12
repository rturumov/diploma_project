from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from forum.models import Message


@admin.register(Message)
class MessageAdmin(TranslationAdmin):
    pass
