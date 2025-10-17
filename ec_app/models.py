from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Login(AbstractUser):
    is_customer =  models.BooleanField(default=False)
    is_seller = models.BooleanField(default= False)

class Customer(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='customer')
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phone=models.CharField(max_length=10)



class Seller(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='seller')
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phone=models.CharField(max_length=10)


class Product_Add(models.Model):
    user = models.ForeignKey(Seller,on_delete=models.CASCADE,related_name='seller_product')
    name=models.CharField(max_length=25)
    description=models.CharField(max_length=200)
    picture= models.FileField(upload_to='products/')
    quantity = models.IntegerField()
    price= models.CharField(max_length=6)
    status=models.IntegerField(default=0)


class Cart(models.Model):
    user=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='cart_products')
    product = models.ForeignKey(Product_Add,on_delete=models.CASCADE,related_name='cart_items')



class Buy(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='user_name')
    product = models.ForeignKey(Product_Add,on_delete=models.CASCADE,related_name='product_name')
    address = models.CharField(max_length=100)
    count = models.IntegerField(default=1)
    phone = models.CharField(max_length=10)
    status = models.IntegerField(default=0)


#migrate after table is created






#we can give any variable name and it will be connected to all data through foreign key concept


