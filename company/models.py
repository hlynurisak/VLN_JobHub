from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    CompanyStart_date = models.DateField(null=True, blank=True)


    location = models.CharField(max_length=255, blank=True)
    link_to_page = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    def get_first_image(self):
        return self.images.first().image
