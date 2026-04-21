from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name