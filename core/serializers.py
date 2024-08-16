from rest_framework.serializers import ModelSerializer;
from .models import Shoe,BrandName

class BrandNameSerializer(ModelSerializer):
    class Meta:
        model =BrandName
        fields ="__all__"




class Shoeerializer(ModelSerializer):
    # product_image =serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model=Shoe
        fields ="__all__"
        