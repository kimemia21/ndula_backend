from django.db import models

class BrandName(models.Model):
    name =models.CharField(max_length=100)
    brand_logo =models.ImageField(upload_to="images/", height_field=None, width_field=None, max_length=None)
    
    def __str__(self) -> str:
        return self.name 
    


class Shoe(models.Model):
    name =models.CharField(max_length=50)
    price = models.FloatField()
    image =models.ImageField( upload_to="images/", height_field=None, width_field=None, max_length=None)
    gender =models.CharField(max_length=50)
    size = models.IntegerField()
    brandName =models.ForeignKey(BrandName,on_delete=models.CASCADE)
    likes =models.IntegerField()
    
    
    def __str__(self):
        return self.name
    
    



    
    
    
    
    


    
    
    

    


    
    

# Create your models here.
