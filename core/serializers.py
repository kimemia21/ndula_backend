from rest_framework.serializers import ModelSerializer;
from .models import products

class productSerializer(ModelSerializer):
    # product_image =serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model=products
        fields ="__all__"
        