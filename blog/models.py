from django.db import models


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
    text = models.TextField
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
