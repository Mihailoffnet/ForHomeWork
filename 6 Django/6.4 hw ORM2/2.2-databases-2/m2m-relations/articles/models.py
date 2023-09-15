from django.db import models

class Tag(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50, verbose_name='Tag')
    slug = models.SlugField(max_length=50, default=None)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['id']
    def __str__(self):
        return f'{self.name}'

class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tag, through='Scope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']
    def __str__(self):
        return f'{self.title}'

class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes', verbose_name='Статьи')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Тэги')
    is_main = models.BooleanField(default=False, verbose_name='Основной тэг')

    class Meta:
        ordering = ['-is_main']
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return f'{self.tag}-{self.is_main}  - {self.article}'