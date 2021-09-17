from django.db import models


class Restaurant(models.Model):
    """The restaurant model"""

    name = models.CharField(max_length=100, unique=True)
