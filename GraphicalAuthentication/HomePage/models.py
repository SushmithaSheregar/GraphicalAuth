from django.db import models

# Create your models here.
class Details(models.Model):
    img_index = models.CharField(max_length=30)
    Username = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    
    


