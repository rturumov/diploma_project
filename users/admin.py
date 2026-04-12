from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from users.models import Answer, EmailVerification, Question, UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(TranslationAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(TranslationAdmin):
    pass
