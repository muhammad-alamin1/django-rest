from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from . models import Bruass
from .serializers import BruassSerializers


@method_decorator(csrf_exempt, name='dispatch')
class Information(APIView):
    # get all dataset or specific data by pk
    def get(self, request, pk=None):
        try:
            if pk:
                complex_data = Bruass.objects.get(id=pk)
                serializer = BruassSerializers(complex_data)
                
                return Response(serializer.data)
            else:
                # complex data
                teacher_complex_data = Bruass.objects.all()
                # convert complex data to py dict
                teacher_serializer_data = BruassSerializers(teacher_complex_data, many=True)
                
                return Response(teacher_serializer_data.data)
        except Bruass.DoesNotExist:
            raise Http404
    
    # post method
    def post(self, request):
        serializer = BruassSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Successfully inserted data.!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
