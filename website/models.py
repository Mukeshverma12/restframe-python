from django.db import models

# Create your models here.
class Website(models.Model):
    title=models.CharField(max_length=255)
    subtitle=models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    isbn = models.CharField(max_length=15)

    def __str__(self):
        return self.title
