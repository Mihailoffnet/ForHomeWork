from django.contrib import admin

from .models import Article, Tag, Scope
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            # print(form.cleaned_data['is_main'])
            if form.cleaned_data['is_main']:
                main += 1
        if main > 1:
            raise ValidationError('Основной тэг должен быть только один')
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            raise ValidationError('Основной тэг должен быть только один')
        else:
            return super().clean()  # вызываем базовый код переопределяемого метода

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at', 'image',]
    inlines = [ScopeInline]
    list_filter = ['id',]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    # inlines = [ScopeInline]
    list_filter = ['name',]

# @admin.register(Scope)
# class ScopeAdmin(admin.ModelAdmin):
#     list_display = ['article', 'tag', 'is_main']
#     list_filter = ['tag',]
