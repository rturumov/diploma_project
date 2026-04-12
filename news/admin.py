from django.contrib import admin, messages
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin
from modeltranslation import settings as mt_settings
from modeltranslation.utils import build_localized_fieldname

from .form import ArticleAdminForm, EventForm, AuthorAdminForm
from .models import (
    Article,
    AutomationCases,
    Category,
    Checklist,
    City,
    Document,
    DraftArticle,
    Event,
    EventCategory,
    EventTag,
    FAQ,
    Instruction,
    Law,
    LegalAct,
    RiskManagement,
    Study,
    Tag,
)
from users.models import Author


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    pass


@admin.register(Tag)
class TagAdmin(TranslationAdmin):
    pass


@admin.register(FAQ)
class FAQAdmin(TranslationAdmin):
    pass


@admin.register(LegalAct)
class LegalActAdmin(TranslationAdmin):
    pass


@admin.register(Document)
class DocumentAdmin(TranslationAdmin):
    pass


@admin.register(Instruction)
class InstructionAdmin(TranslationAdmin):
    pass


@admin.register(Law)
class LawAdmin(TranslationAdmin):
    pass


@admin.register(Study)
class StudyAdmin(TranslationAdmin):
    pass


@admin.register(EventTag)
class EventTagAdmin(TranslationAdmin):
    pass


@admin.register(EventCategory)
class EventCategoryAdmin(TranslationAdmin):
    pass


@admin.register(City)
class CityAdmin(TranslationAdmin):
    pass


@admin.register(Checklist)
class ChecklistAdmin(TranslationAdmin):
    pass


@admin.register(AutomationCases)
class AutomationCasesAdmin(TranslationAdmin):
    pass


@admin.register(RiskManagement)
class RiskManagementAdmin(TranslationAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    form = ArticleAdminForm
    readonly_fields = ('image_preview',)

    def get_exclude(self, request, obj=None):
        # TranslationAdmin only applies the form's Meta.exclude when ModelAdmin.exclude
        # is empty; readonly_fields make exclude non-empty, so we must drop `image` here
        # (JSON in admin) and keep using `new_image` on ArticleAdminForm.
        ex = list(super().get_exclude(request, obj) or [])
        if 'image' not in ex:
            ex.append('image')
        return tuple(ex)

    def image_preview(self, obj):
        if obj.image and obj.image.get('path'):
            return format_html(
                '<img src="{}" style="max-height: 200px; max-width: 200px;" />',
                obj.image['path']
            )
        return "No image uploaded"

    image_preview.short_description = 'Current Image'


def _copy_translated_fields(source, target, field_names):
    """Copy localized columns from draft to article (fallback to legacy base field for RU)."""
    for base in field_names:
        for lang in mt_settings.AVAILABLE_LANGUAGES:
            loc = build_localized_fieldname(base, lang)
            val = getattr(source, loc, None)
            if val in (None, "") and lang == mt_settings.DEFAULT_LANGUAGE:
                val = getattr(source, base, None)
            if val is not None and val != "":
                setattr(target, loc, val)


@admin.action(description="Опубликовать")
def publish_draft_articles(modeladmin, request, queryset):
    created_count = 0

    for draft in queryset:
        article = Article(image=draft.image or {}, alias=draft.alias or None)
        _copy_translated_fields(draft, article, ("title", "description", "content"))
        article.save()

        article.tags.set(draft.tags.all())
        article.categories.set(draft.categories.all())

        created_count += 1

    messages.success(request, f"{created_count} черновик(ов) опубликовано как новости.")


@admin.register(DraftArticle)
class DraftArticleAdmin(TranslationAdmin):
    list_display = ('title', 'datetime_created')
    actions = [publish_draft_articles]


@admin.register(Event)
class EventAdmin(TranslationAdmin):
    form = EventForm


@admin.register(Author)
class AuthorAdmin(TranslationAdmin):
    form = AuthorAdminForm
