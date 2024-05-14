from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

'''def index (request):
    return render(request,'index.html')

'''

@api_view (['GET'])
def getall (request):
    if request.method=='GET':
        bdata=Book.objects.all()
        serial=BookSerializer(bdata,many=True)
        return Response (serial.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST )


@api_view (['GET'])
def getid (request,id ):
    try:
        bid=Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)  

    serial=BookSerializer(bid)
    return Response (serial.data,status=status.HTTP_200_OK)      


@api_view (['DELETE',])
def deleteid (request,id):
    try:
        bid=Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)  
    if request.method=='DELETE':
        Book.delete(bid)
        return  Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
