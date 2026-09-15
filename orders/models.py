from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

class Order(models.Model):
    class Status(models.TextChoices):
        CART=("cart","в корзине")
        CREATED=("created","оформлен")
        TRANSIT=("transit","в пути")
        COMPLETE=("complete","доставлен")
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    status=models.CharField(max_length=12,choices=Status)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.user.username} - {self.product.name} Статус: {self.status}'
