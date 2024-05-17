from django.db import models
from JobHub.models import Job, Company, User


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return self.full_name


class CoverLetter(models.Model):
    text = models.TextField()

    def __str__(self):
        return f"Cover Letter ({self.id})"


class Experience(models.Model):
    place_of_work = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.role} at {self.place_of_work}"


class Recommendation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    role = models.CharField(max_length=255)
    may_be_contacted = models.BooleanField()

    def __str__(self):
        return f"Recommendation by {self.name}"


class Application(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    experience = models.ForeignKey(Experience, on_delete=models.SET_NULL, related_name='applications', blank=True, null=True)
    recommendation = models.ForeignKey(Recommendation, on_delete=models.SET_NULL, related_name='applications', blank=True, null=True)
    cover_letter = models.ForeignKey(CoverLetter, on_delete=models.SET_NULL, related_name='applications', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Reviewed', 'Reviewed'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted')])

    def __str__(self):
        return f"Application for {self.job.name} at {self.company.name} by {self.applicant.username}"

    class Meta:
        ordering = ['-created_at']
