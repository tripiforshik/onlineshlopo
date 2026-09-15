from django.shortcuts import render

def cart(request):
    return render(request,"orders/cart.html")

def delivery(request):
    return render(request,"orders/delivery.html")

def completed(request):
    return render(request,"orders/completed.html")
