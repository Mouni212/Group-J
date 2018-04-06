from django.db import models

# Create your models here.
class Jobs(models.Model):
    job_title=models.CharField(max_length=500)
    job_category=models.CharField(max_length=250)
    job_location=models.CharField(max_length=250)

    def __str__(self):
        return self.job_title
