from django.urls import path,include,re_path
from .views import ShoesApi,BrandNameApi,Cart,CartItem
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("shoes",view=ShoesApi.as_view()),
    path("brandname",view=BrandNameApi.as_view()),
    path("shoes/<int:pk>",view=ShoesApi.as_view()),
    
    path("cart",view=Cart.as_view()),
    
    path("cartItem",view=CartItem.as_view())
    
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
