from django.db import models
from company.models import Company

# Create your models here.
class JobCategory(models.Model):
    name = models.CharField(max_length=255)

class Job(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    job_requirements = models.FloatField
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class companyimage(models.Model):
    name = models.CharField(max_length=9999)
    Job = models.ForeignKey(Job, on_delete=models.CASCADE)

