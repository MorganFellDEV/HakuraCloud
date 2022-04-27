from django import forms
from django.forms import ModelForm

from hakura.models import User, Post

import django.contrib.auth.models

class NewPostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('UserID',)


    # def save(self):
    #     data = self.cleaned_data
    #     post = Post(PostContent=data['content'])
    #     post.save()