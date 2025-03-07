from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.
class Main_category(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=20)
    categories=models.ForeignKey(Main_category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField(max_length=200)
    image=models.ImageField(upload_to="product",null=True,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

