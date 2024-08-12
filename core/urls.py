from django.urls import path,include,re_path
from .views import getProducts
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("all", view=getProducts),
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
