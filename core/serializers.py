from rest_framework import serializers
from .models import Shoe, BrandName,Cart,CartItem
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import User

class BrandNameSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()

    class Meta:
        model = BrandName
        fields = ["name", "brand_logo", "logo_url"]

    def get_logo_url(self, obj):
        if obj.brand_logo:
            return self.context["request"].build_absolute_uri(obj.brand_logo.url)
        return None

class ShoeSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brandName.name', read_only=True)
    brand_details = BrandNameSerializer(source='brandName', read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Shoe
        fields = ['id', 'name', 'price', 'image', 'image_url', 'gender', 'size', 'brandName', 'brand_name', 'brand_details', 'likes',"description"]

    def get_image_url(self, obj):
        if obj.image:
            return self.context["request"].build_absolute_uri(obj.image.url)
        return None
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields =("id", "username", "email")



    
class CartItemSerilization(serializers.ModelSerializer):
    
    class Meta:
        model=CartItem
        fields =("id,","cart","shoe","name")
        
class CartSerilization(serializers.ModelSerializer):
    items =CartItemSerilization(many=True,source="cartitem_set",read_only=True)
    
    class Meta:
        model =Cart
        fields =("id", "user","name", "items")       
        
    
        
    