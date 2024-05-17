from django.db import models
<<<<<<< Updated upstream
from JobHub.models import Job, Company, User
=======
from JobHub.models import Job
>>>>>>> Stashed changes


class ContactInformation(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='contact_info')
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name


class CoverLetter(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='cover_letters')
    cover_letter = models.TextField()

    def __str__(self):
        return f"Cover Letter ({self.id})"


class Experience(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='experiences')
    workplace = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.role} at {self.place_of_work}"


class Recommendation(models.Model):
<<<<<<< Updated upstream
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
=======
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='recommendations')
    rec_name = models.CharField(max_length=100)
    rec_email = models.EmailField()
    rec_phone = models.CharField(max_length=15)
    rec_role = models.CharField(max_length=100)
    rec_contact = models.BooleanField(default=False)
>>>>>>> Stashed changes
