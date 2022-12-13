from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticlesScopes, Tags


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_main = 0
        tags_list = []
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count_main += 1
            if count_main > 1:
                raise ValidationError('Основной тег уже отмечен')
            if form.cleaned_data.get('tag') in tags_list:
                raise ValidationError('Такой тег уже есть')
            elif form.cleaned_data.get('tag') is not None:
                tags_list.append(form.cleaned_data.get('tag'))


class ScopesInline(admin.TabularInline):
    model = ArticlesScopes
    extra = 3
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopesInline, ]


@admin.register(Tags)
class ArticleAdmin(admin.ModelAdmin):
    pass
