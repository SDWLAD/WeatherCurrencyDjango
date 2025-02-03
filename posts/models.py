from django.db import models
import datetime

class Article(models.Model):
    views = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=300)
    date = models.DateTimeField(default=datetime.datetime.utcnow)
    def __repr__(self):
        return '<Article%r>' % self.id

class Comment(models.Model):
    article_id = models.IntegerField()
    text = models.TextField(max_length=300)
    date = models.DateTimeField(default=datetime.datetime.utcnow)
    def __repr__(self):
        return '<Comment%r>' % self.id