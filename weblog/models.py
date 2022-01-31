from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100 )
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment (models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
