from django.contrib.auth.models import User
from django.db import models
from company.models import Company


class JobCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    job_requirements = models.CharField(max_length=255, blank=True)
    due_date = models.DateField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_type = models.CharField(
        max_length=2,
        choices=[('FT', 'Full-time'), ('PT', 'Part-time')],
        default='FT')

    def __str__(self):
        return self.name


class JobRequirement(models.Model):
    requirement = models.CharField(max_length=255)
    Job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return self.requirement


class CompanyImage(models.Model):
    image = models.URLField(max_length=9999)
    company = models.ForeignKey(Company, related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return self.image

