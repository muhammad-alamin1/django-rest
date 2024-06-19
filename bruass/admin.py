from django.contrib import admin
from . models import Bruass

# Register your models here.
class BruassAdmin(admin.ModelAdmin):
    list_display = ["id", "teacher_name", "course_name", "course_duration", "seat"]
    

admin.site.register(Bruass, BruassAdmin)