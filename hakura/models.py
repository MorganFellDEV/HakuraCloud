import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.



class User(AbstractUser):
    UserDisplayName = models.CharField(max_length=32)
    UserBio = models.CharField(max_length=140, null=True)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    PostContent = models.CharField(max_length=140)
