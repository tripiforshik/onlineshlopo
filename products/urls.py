from django.urls import path
from .views import  catalog


urlpatterns = [
    path('catalog',catalog,name='catalog')

]