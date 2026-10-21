from django.shortcuts import render,redirect
from django.views.generic import ListView
from orders.models import Order
from accounts.models import Profile

class CartListView(ListView):
    model=Order
    template_name = 'orders/cart.html'
    context_object_name = 'order_list'
    def get_queryset(self):
        queryset=super().get_queryset()
        queryset=queryset.filter(user=self.request.user,status=Order.Status.CART)
        self.total=0
        if queryset:
            for order in queryset:
                self.total+=order.product.price
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context ['total']=self.total
        profile=Profile.objects.get(user=self.request.user)

        context ["profile"]=profile
        return context
def delivery(request):
    return render(request,"orders/delivery.html")

def completed(request):
    return render(request,"orders/completed.html")
