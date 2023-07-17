from django.db import models


class ShortenedURL(models.Model):
    objects = None
    long_url = models.CharField(max_length=300)
    short_url = models.CharField(max_length=100)
