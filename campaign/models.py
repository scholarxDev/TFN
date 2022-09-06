from django.db import models

# Create your models here.

class Campaign(models.Model):
    title = models.CharField(max_length=255)
    campaign_objective = models.TextField()
    duration = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


