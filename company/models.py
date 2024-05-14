from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    CompanyStart_date = models.DateTimeField()
    logo = models.CharField(max_length=9999, blank=True)

    def __str__(self):
        return self.name