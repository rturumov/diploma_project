from modeltranslation.translator import TranslationOptions, register

from .models import (
    Article,
    ArticleComment,
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
    FixedMenu,
    Instruction,
    Law,
    LawComment,
    LegalAct,
    Qauipmedia,
    RiskManagement,
    Study,
    Tag,
)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("title", "seo_text", "desc")


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ("title", "description", "seo_tag", "tag_name")


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ("title", "description", "content")


@register(DraftArticle)
class DraftArticleTranslationOptions(TranslationOptions):
    fields = ("title", "description", "content")


@register(ArticleComment)
class ArticleCommentTranslationOptions(TranslationOptions):
    fields = ("text", "author_full_name")


@register(FixedMenu)
class FixedMenuTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Instruction)
class InstructionTranslationOptions(TranslationOptions):
    fields = ("title", "description", "author")


@register(Document)
class DocumentTranslationOptions(TranslationOptions):
    fields = ("title", "description", "topics")


@register(RiskManagement)
class RiskManagementTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(AutomationCases)
class AutomationCasesTranslationOptions(TranslationOptions):
    fields = ("title", "description", "company")


@register(Checklist)
class ChecklistTranslationOptions(TranslationOptions):
    fields = ("title", "use_case")


@register(Qauipmedia)
class QauipmediaTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(Law)
class LawTranslationOptions(TranslationOptions):
    fields = ("title", "description", "topics")


@register(LawComment)
class LawCommentTranslationOptions(TranslationOptions):
    fields = ("text", "author_full_name")


@register(Study)
class StudyTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(LegalAct)
class LegalActTranslationOptions(TranslationOptions):
    fields = ("title", "summary")


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ("question", "answer", "author", "author_profession")


@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(EventCategory)
class EventCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(EventTag)
class EventTagTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ("title", "description", "author_full_name", "author_job_title")
