from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    text = models.TextField()
    date = models.DateTimeField()
    likes = models.IntegerField(default=0)
    isActive = models.BooleanField(default=1)


class Comment(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now())
    text = models.TextField(default="")
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
