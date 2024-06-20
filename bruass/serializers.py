from rest_framework import serializers
from .models import Bruass


class BruassSerializers(serializers.Serializer):
    teacher_name = serializers.CharField(max_length=25)
    course_name = serializers.CharField(max_length=25)
    course_duration = serializers.IntegerField()
    seat = serializers.IntegerField()
    
    def create(self, validated_data):
        return Bruass.objects.create(**validated_data)