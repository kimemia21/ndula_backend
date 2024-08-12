from django.db import models

class products(models.Model):
    name =models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image =models.ImageField( upload_to="images/", height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.name
    
    

# Create your models here.
