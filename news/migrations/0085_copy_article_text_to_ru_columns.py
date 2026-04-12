# Generated manually: copy legacy title/description/content into *_ru columns
# so modeltranslation reads correct Russian text after 0084.

from django.db import migrations


def copy_ru_fields(apps, schema_editor):
    Article = apps.get_model("news", "Article")
    for row in Article.objects.values("id", "title", "description", "content"):
        Article.objects.filter(pk=row["id"]).update(
            title_ru=row["title"] or "",
            description_ru=row["description"],
            content_ru=row["content"] or "",
        )


def noop_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0084_article_i18n_fields"),
    ]

    operations = [
        migrations.RunPython(copy_ru_fields, noop_reverse),
    ]
