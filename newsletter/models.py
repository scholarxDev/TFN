from django.db import models

# Create your models here.

class Newsletter (models.Model):
    email = email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
