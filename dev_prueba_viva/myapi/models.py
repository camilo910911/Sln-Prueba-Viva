from django.db import models
from django.db.models import CharField, Model
from django_mysql.models import ListCharField

# Create your models here.


# used to be useb for save info in database of project. Before redis server

"""
class TopStories(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    num = models.PositiveIntegerField()

class DetailStory(models.Model):
    by = models.CharField(max_length=200)
    descendants = models.PositiveIntegerField()
    story_id = models.PositiveIntegerField(primary_key=True)
    kids = ListCharField(
        base_field = models.PositiveIntegerField(),
        max_length=(50),
    )
    score = models.PositiveIntegerField()
    time = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    url = models.CharField(max_length=100)
"""




