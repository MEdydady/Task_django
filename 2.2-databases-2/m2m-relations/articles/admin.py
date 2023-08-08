from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag_is_selected = False
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data["is_main"]:
                if main_tag_is_selected:
                    raise ValidationError("Основным может быть только один раздел")
                else:
                    main_tag_is_selected = True
        if not main_tag_is_selected:
            raise ValidationError("Укажите основной раздел")
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (ScopeInline,)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
