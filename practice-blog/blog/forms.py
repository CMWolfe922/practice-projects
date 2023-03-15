from django import forms
from .models import Blog, Comment

class BlogForm(forms.Form):

    class Meta:
        model = Blog


class CommentForm(forms.Form):


    class Meta:
        model = Comment
        managed = True
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
