from django.shortcuts import get_object_or_404;

from rest_framework.response import Response;
from rest_framework.decorators import api_view,APIView;
from  rest_framework import status;
# from django.contrib.auth.models import User;
from .models import Shoe,BrandName,Cart,CartItem;
from .serializers import ShoeSerializer,BrandNameSerializer;


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
        serializer =ShoeSerializer(shoe,many=True,context={"request":request})
        
      
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,*args, **kwargs):
        data =request.data
        if data["action"]=="createShoe":
            return self.createShoe(request)
            
                
            
        
      
    def createShoe(self,request):
        data =request.data
        serializer =ShoeSerializer(data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request,pk):
    
        data =request.data
        if "likes" in data:
            likes =data["likes"]
            shoes =get_object_or_404(Shoe,id=pk)
            shoes.likes=likes
            print(shoes.likes)
            shoes.save()
            serializer =ShoeSerializer(shoes,context={"request":request})
            return Response({"message":"likes added",
                             "data":serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"please add like to the request"},status=status.HTTP_400_BAD_REQUEST)
        
class Cart(APIView):
    def get(self, request ):
        cart =Cart.objects.all()
        serializer =ShoeSerializer(cart, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        data =request.data
        serializer =ShoeSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CartItem(APIView):
    def post(self,request):
        data =request.data
        serilizer =CartItem(data=data,many=True)
        if serilizer.is_valid():
            serilizer.save()
            return Response({"message":"sucess"})
        else:
            return Response({"message":"serilizer is invalid"},status=status.HTTP_201_CREATED)
    def get(self,request):
        cartItem =CartItem.objects.all()
        serializer =CartItem(cartItem, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
        

                   
                    
                 
                
        





# @api_view(["GET"])
# def getShoe(request):
#     obj=Shoe.objects.all()
#     serializer =ShoeSerializer(obj,many=True)
#     return Response(serializer.data,status=status.HTTP_200_OK)

# @api_view(["POST"])
# def post_product(reqeust):
#     data =reqeust.data
#     serializer =ShoeSerializer(data=data,many=True)
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
#    serializer =ShoeSerializer(data=data,partial=True) 
#    if serializer.is_valid():
#        serializer.save()
#        return Response(serializer.data,status=status.HTTP_200_OK)
#    else:
#        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
    
      
            

  


# Create your views here.
