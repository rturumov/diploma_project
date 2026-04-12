from modeltranslation.translator import TranslationOptions, register

from .models import Answer, Author, Question


@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ("name", "profession", "description")


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(Answer)
class AnswerTranslationOptions(TranslationOptions):
    fields = ("content",)
