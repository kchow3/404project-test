import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Author(AbstractBaseUser):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    profile_img = models.ImageField()
    host = models.CharField(max_length=2000)
    author_url = models.CharField(max_length=2000)

class Post(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    date_created = models.DateField()
    image = models.ImageField()
