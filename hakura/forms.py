from django import forms
from hakura.models import User, Post


class NewPostForm(forms.Form):
    userID = forms.UUIDField()
    content = forms.CharField(max_length=128)

    def save(self):
        data = self.cleaned_data
        post = Post(UserID=User.objects.get(id=data['userID']),PostContent=data['content'])
        post.save()