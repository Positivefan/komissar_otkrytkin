from django.db import models

# Create your models here.


class Article(models.Model):
    article_title = models.CharField('название статьи', max_length=200)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.article_title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('имя автора', max_length=50)
    comment_text = models.CharField('текст комментария', max_length=200)

    def __str__(self):
        return self.author_name


class Createpost(models.Model):
    post = models.CharField('название статьи', max_length=200)
    post_name = models.TextField('текст статьи')
    post_text = models.DateTimeField('дата публикации')