from django.urls import path
from .views import ProductListView,ProductDetailView


urlpatterns = [
    path('catalog',ProductListView.as_view(),name='catalog'),
    path ('<slug:slug>',ProductDetailView.as_view(),name='product_detail'),

]