from __future__ import unicode_literals

from django.db import models



class Snippet(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):
        options = self.username and {'username': self.username} or {}
        super(Snippet, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created',)

class Error(models.Model):

    error=models.CharField(max_length=200)
    def __init__(self, error):
        self.error=error

