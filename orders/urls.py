from django.urls import path
from .views import CartListView,delivery,completed


urlpatterns = [
    path('completed',completed,name='completed'),
    path('delivery',delivery,name='delivery'),
    path('cart',CartListView.as_view(),name='cart'),

]