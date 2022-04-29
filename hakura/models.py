import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    UserDisplayName = models.CharField(max_length=32)
    UserBio = models.CharField(max_length=140, null=True)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    PostContent = models.CharField(max_length=140)


class Follow(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    target = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")