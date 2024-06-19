from django.db import models

# Create your models here.
class Bruass(models.Model):
    teacher_name = models.CharField(max_length=25)
    course_name = models.CharField(max_length=25)
    course_duration = models.IntegerField()
    seat = models.IntegerField()