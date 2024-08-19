from django.urls import path,include,re_path
from .views import ShoesApi,BrandNameApi
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("shoes",view=ShoesApi.as_view()),
    path("brandname",view=BrandNameApi.as_view()),
    path("shoes/<int:pk>",view=ShoesApi.as_view())
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
