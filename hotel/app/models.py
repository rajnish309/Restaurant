from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    desc=models.TextField(max_length=200)
    phone=models.IntegerField()
def __str__(self):
        return self.name

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    Sub_category=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    image=models.ImageField(upload_to="images/images.png")

    def __str__(self):
        return self.product_name