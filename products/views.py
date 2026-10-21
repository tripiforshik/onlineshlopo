
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from .models import Product
from orders.models import Order

class ProductListView(ListView):
    model = Product
    template_name='products/catalog.html'
    context_object_name = 'product_list'

class ProductDetailView(DetailView):
    model=Product
    context_object_name = 'product'
    def get_object(self,queryset=None):
        slug=self.kwargs.get('slug')
        products=Product.objects.filter(slug=slug).exclude(count=0)
        first_product=products.first()
        sizes=[]
        for product in products:
            sizes.append(product.size)
        first_product.size_variants=sizes
        return first_product
    def post(self,request,*args,**kwargs):
        current_slug=self.kwargs.get('slug')
        selected_size=request.POST.get("sizes")
        print(current_slug,selected_size)
        selected_product=Product.objects.get(slug=current_slug,size=selected_size)
        Order.objects.create(user=request.user,product=selected_product,status=Order.Status.CART)
        return redirect('cart')