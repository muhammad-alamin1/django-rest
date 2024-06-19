from django.shortcuts import render
from django.views import View
from . models import Bruass
from .serializers import BruassSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

#queryset
class Information(View):
    # get all dataset
    def get(self, request, pk=None):
        if pk:
            complex_data = Bruass.objects.get(id=pk)
            serializer = BruassSerializers(complex_data)
            json_data = JSONRenderer().render(serializer.data)
            
            return HttpResponse(json_data, content_type='application/json')
        else:
            # complex data
            teacher_complex_data = Bruass.objects.all()
            # convert complex data to py dict
            teacher_serializer_data = BruassSerializers(teacher_complex_data, many=True)
            # render JSON
            json_data = JSONRenderer().render(teacher_serializer_data.data)
            
            return HttpResponse(json_data, content_type='application/json')
    