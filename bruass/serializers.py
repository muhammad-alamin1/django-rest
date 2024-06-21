from rest_framework import serializers
from .models import Bruass


# model serializers
class BruassSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bruass
        fields = '__all__' # or
        # fields = ['teacher_name', 'course_name', 'course_duration', 'seat']
