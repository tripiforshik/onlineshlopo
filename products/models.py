from django.db import models
class Size(models.Model):
    size=models.CharField(max_length=12,primary_key=True)

class Color(models.Model):
    color=models.CharField(max_length=12,primary_key=True)

class Category(models.Model):
    category=models.CharField(max_length=12,primary_key=True)


class Product(models.Model):
    name=models.CharField(max_length=150)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(blank=True,upload_to='products')
    count=models.IntegerField()
    slug=models.SlugField()