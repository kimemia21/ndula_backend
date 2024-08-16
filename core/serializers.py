from rest_framework import serializers;
from .models import Shoe,BrandName

class BrandNameSerializer(serializers.ModelSerializer):
    logo_url =serializers.SerializerMethodField()
    
    
    class Meta:
        model =BrandName
        fields =["name","logo,","logo_url"]
    
    def get_image_url(self,obj):
        if obj.image:
            
            return self.context["request"].build_absolute_uri(obj.image.url)
        return None
            
        




class Shoeerializer(serializers.ModelSerializer):
    # product_image =serializers.ImageField(max_length=None, use_url=True)
    brand_name =BrandNameSerializer(read_only=True)
    image_url =serializers.SerializerMethodField()
    class Meta:
        model=Shoe
        fields = ['id', 'name', 'price', 'image', 'image_url', 'gender', 'size', 'brandName', 'brand_name', 'likes']
    def get_image_url(self,obj):
        if obj.image:
            
            return self.context["request"].build_absolute_uri(obj.image.url)
        return None    

        