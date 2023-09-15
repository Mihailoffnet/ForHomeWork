from django.shortcuts import render

from articles.models import Article, Tag


def articles_list(request):
    template = 'articles/news.html'
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    # модуль для вывода статей по тегам
    tag_name = request.GET.get('tag_name', None)
    # print(tag_name)
    # print(Article.objects.filter(scopes__is_main=True))
    if tag_name:
         object_list = Article.objects.filter(scopes__tag__slug=tag_name).order_by(ordering)
    else:
        object_list = Article.objects.order_by(ordering)

    # for article in object_list:
    #     print(article.title)
    #     print(article.published_at)
    #     print(article.scopes.all())
    #     for scope in article.scopes.all():
    #         print(scope.tag.slug)
    context = {
        'object_list': object_list
    }

    return render(request, template, context)
