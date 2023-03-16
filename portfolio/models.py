from django.db import models
from django.db.models import ImageField
from django.db.models.fields import CharField, URLField


class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to='portfolio/images')
    url = URLField(blank=True)
