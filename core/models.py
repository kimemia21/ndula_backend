from django.db import models
from django.contrib.auth.models import User;

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
    description =models.TextField(default="no description",blank=True)
    
    
    def __str__(self):
        return self.name


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at =models.DateField(auto_now_add=True,)
    name =models.CharField(max_length=150)
    
    def save(self, *args, **kwargs):
        self.name =self.user.username
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return self.name
    
    
    
    
    
class CartItem(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    cart =models.ForeignKey(Cart, on_delete=models.CASCADE)   
    shoe =models.ForeignKey(Shoe, on_delete=models.CASCADE)
    name =models.CharField(max_length=150) 
    
    def save(self,*args, **kwargs):
        self.name =self.shoe.name
        super().save(*args, **kwargs) 
        






    



    
    
    
    
    


    
    
    

    


    
    

# Create your models here.
