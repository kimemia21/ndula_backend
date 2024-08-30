from django.urls import path,include,re_path
from .views import ShoesApi,BrandNameApi,CartView,CartItemView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("shoes",view=ShoesApi.as_view()),
    path("brandname",view=BrandNameApi.as_view()),
    path("shoes/<int:pk>",view=ShoesApi.as_view()),
    
    path("cart",view=CartView.as_view()),
    
    path("cartItem",view=CartItemView.as_view())
    
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
