from django.urls import path
from .views import cart,delivery,completed


urlpatterns = [
    path('completed',completed,name='completed'),
    path('delivery',delivery,name='delivery'),
    path('cart',cart,name='cart'),

]