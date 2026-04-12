from django import forms
from trix_editor.widgets import TrixEditorWidget
from .models import Article, ArticleComment, LawComment, Event, Author


class ArticleAdminForm(forms.ModelForm):
    new_image = forms.ImageField(label='Картинки', required=False)

    class Meta:
        model = Article
        exclude = ['image']
        widgets = {
            "content": TrixEditorWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == "content" or name.startswith("content_"):
                field.widget = TrixEditorWidget()

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data.get('new_image'):
            # handle the image save yourself
            image = self.cleaned_data['new_image']
            from django.core.files.storage import default_storage
            path = default_storage.save(f'uploads/{image.name}', image)
            url = default_storage.url(path)

            # update the JSONField
            if not instance.image:
                instance.image = {}
            instance.image['path'] = url

        if commit:
            instance.save()
        return instance


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['text']


class LawCommentForm(forms.ModelForm):
    class Meta:
        model = LawComment
        fields = ['text']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            "description": TrixEditorWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == "description" or name.startswith("description_"):
                field.widget = TrixEditorWidget()


class AuthorAdminForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
            "description": TrixEditorWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == "description" or name.startswith("description_"):
                field.widget = TrixEditorWidget()