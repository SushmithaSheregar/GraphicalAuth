from django.db import models
from numpy import byte

# Create your models here.
class Details(models.Model):
    img_index = models.CharField(max_length=30, default='')
    Username = models.CharField(max_length=30, default='')
    email = models.EmailField()
    phone = models.CharField(max_length=30, default='')
    imageBytes = models.BinaryField(default=bytes('', encoding='utf-8'), editable=True) 
    # ImageField(upload_to="images_db",default="")

class GeeksModel(models.Model):
    geeks_field = models.BinaryField(editable=True)
    
    


