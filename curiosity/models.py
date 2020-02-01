from django.db import models

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Post(models.Model):
    question = models.CharField(max_length=1000, verbose_name='title')
    answer = MarkdownxField()
    pub_date = models.DateField(verbose_name='date')

    @property
    def formatted_markdown(self):
        return markdownify(self.answer)

    def peek(self):
        return self.formatted_markdown[:500]

    def __str__(self):
        return self.question

    class Meta():
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'