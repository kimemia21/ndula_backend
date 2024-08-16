from django.shortcuts import get_object_or_404;

from rest_framework.response import Response;
from rest_framework.decorators import api_view,APIView;
from  rest_framework import status;
# from django.contrib.auth.models import User;
from .models import Shoe,BrandName;
from .serializers import Shoeerializer,BrandNameSerializer;


class BrandNameApi(APIView):
    def get(self,request):
        brandName =BrandName.objects.all()
        serializer =BrandNameSerializer(brandName,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        data =request.data
        serializer =BrandNameSerializer(data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ShoesApi(APIView):
    
    def get(self,request):
        shoe =Shoe.objects.all()
        serializer =Shoeerializer(shoe,many=True,context={"request":request})
        
      
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        data =request.data
        serializer =Shoeerializer(data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        





# @api_view(["GET"])
# def getShoe(request):
#     obj=Shoe.objects.all()
#     serializer =Shoeerializer(obj,many=True)
#     return Response(serializer.data,status=status.HTTP_200_OK)

# @api_view(["POST"])
# def post_product(reqeust):
#     data =reqeust.data
#     serializer =Shoeerializer(data=data,many=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     else:
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
# @api_view(["PATCH"])
# def pathProduct(request,pk):
#    id =pk
#    data =request.data
   
#    product =get_object_or_404(Shoe,id =id)
#    serializer =Shoeerializer(data=data,partial=True) 
#    if serializer.is_valid():
#        serializer.save()
#        return Response(serializer.data,status=status.HTTP_200_OK)
#    else:
#        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
    
      
            

  


# Create your views here.
