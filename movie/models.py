from os import name
from sqlite3 import IntegrityError
from turtle import title
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Post(models.Model):
    title=models.CharField(max_length=255)
    text=models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    score = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)], default=0)
    text = models.TextField()
    posted_dated = models.DateTimeField(auto_now_add=True)
