from django import forms
from django.db import models
from django.forms.widgets import Widget

# Create your models here.

format_choice = (('.png', '.png'),('.jpg', '.jpg'),('.pdf', '.pdf'),)


class Image(models.Model):
    image = models.ImageField(upload_to='userimg')
    desired_format = models.CharField(max_length=10, choices=format_choice)

