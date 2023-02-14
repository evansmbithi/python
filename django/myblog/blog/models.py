from django.db import models
from django.utils import timezone

# we want the post class to be a child of the base model class.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=150, null=True)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
