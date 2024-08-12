from django.shortcuts import get_list_or_404;
from rest_framework.response import Response;
from rest_framework.decorators import api_view;
from  rest_framework import status;
from django.contrib.auth.models import User;
from .models import products;
from .serializers import productSerializer;

@api_view(["GET"])
def getProducts(request):
    obj=products.objects.all()
    serializer =productSerializer(obj,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(["POST"])
def post_product(reqeust):
    data =reqeust.data
    serializer =productSerializer(data=data,many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            

  


# Create your views here.
