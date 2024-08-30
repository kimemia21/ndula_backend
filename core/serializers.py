from rest_framework import serializers
from .models import Shoe, BrandName,Cart,CartItem

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
    
class CartItemSerilization(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields =("id,","cart","shoe")
        
class CartSerilization(serializers.ModelSerializer):
    class Meta:
        model =Cart
        fields ="__all__"        
        
    
        
    