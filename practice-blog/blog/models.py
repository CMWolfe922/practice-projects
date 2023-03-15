from django.db import models


# Create your models here.
class Postable(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Blog(Postable):
    title = models.CharField(max_length=255)


class Comment(Postable):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
