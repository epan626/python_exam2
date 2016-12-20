from __future__ import unicode_literals
from ..regandlogin.models import User
from django.db import models

# Create your models here.

class QuotesManager(models.Manager):
    def validate_quote(self, form_data):
        errors = []
        if len(form_data['author']) == 0:
            errors.append('Author can not be blank!')
        if len(form_data['message']) <= 10:
            errors.append('Message has be over 10 characters!')
        return errors

class Quotes(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=50)
    user = models.ForeignKey('regandlogin.User', related_name='user_quote')
    fave = models.ManyToManyField('regandlogin.User', related_name='user_fave')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuotesManager()
