from django.forms import ModelForm
from hakura.models import User, Post


class NewPostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('UserID',)
