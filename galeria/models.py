from django.db import models

# Create your models here.

class Photography(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    subtitle = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    photo_reference = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return f"Photo [title={self.title}]"