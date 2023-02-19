from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Photographies(models.Model):

    CATEGORY_ENUMS = [
        ("NEBULA", "Nebula"),
        ("STAR", "Star"),
        ("GALAXY", "Galaxy"),
        ("PLANET", "Planea"),
    ]

    title = models.CharField(max_length=100, null=False, blank=False)
    subtitle = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False, choices=CATEGORY_ENUMS, default="")
    description = models.TextField(null=False, blank=False)
    photo_reference = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/")
    date = models.DateField(default=datetime.now, blank=False)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False
    )

    def __str__(self):
        return self.title