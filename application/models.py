from django.db import models
from JobHub.models import Job, Company
from django.contrib.auth.models import User


class ContactInformation(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class CoverLetter(models.Model):
    cover_letter = models.TextField()

    def __str__(self):
        return f"Cover Letter ({self.id})"


class Application(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    contact_info = models.ForeignKey(ContactInformation, on_delete=models.CASCADE, related_name='applications', blank=True, null=True)
    cover_letter = models.ForeignKey(CoverLetter, on_delete=models.SET_NULL, related_name='applications', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Reviewed', 'Reviewed'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted')])

    def __str__(self):
        return f"Application for {self.job.name} at {self.company.name} by {self.applicant.username}"

    class Meta:
        ordering = ['-created_at']


class Recommendation(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='recommendations', null=True, blank=True)
    rec_name = models.CharField(max_length=100)
    rec_email = models.EmailField()
    rec_phone = models.CharField(max_length=15)
    rec_role = models.CharField(max_length=100)
    rec_contact = models.BooleanField(default=False)

    def __str__(self):
        return f"Recommendation by {self.rec_name}"


class Experience(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='experiences', null=True, blank=True)
    workplace = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.role} at {self.workplace}"