from django.db import models


class University(models.Model):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=64)
    alpha_two_code = models.CharField(max_length=2)
    web_page = models.URLField(null=True, default=None)
