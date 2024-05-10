from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    advertisement_created = models.DateTimeField()
    logo = models.CharField(max_length=9999, blank=True)
