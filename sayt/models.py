from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    surname = models.CharField(max_length=128, null=True, blank=True)
    subject = models.CharField(max_length=128, null=True, blank=True)
    email = models.CharField(max_length=128)
    message = models.TextField()

    def __str__(self):
        return self.name