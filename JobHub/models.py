from django.db import models
from company.models import Company

# Create your models here.
class JobCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Job(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    job_requirements = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CompanyImage(models.Model):
    image = models.URLField(max_length=9999)
    company = models.ForeignKey(Company, related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return self.image

