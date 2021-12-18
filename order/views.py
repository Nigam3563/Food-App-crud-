from django.shortcuts import render
from django.views.generic import FormView,CreateView,ListView,UpdateView
from order.forms import *
from order.models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.edit import DeleteView
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse


class ShowpageView(ListView):
    model=OrderItem
    form_class=OrderItemForm
    template_name="order/show.html"
    # success_url ="/order:form/"
    context_object_name="orders"

class OrderFormview(CreateView):
    def get(self, request,*args, **kwargs):
                orders = OrderForm(prefix= "orders")
                items = OrderItemForm(prefix="items")

                return render(request, "order/form.html", {
                'orders': orders,
                'items': items,
                })
    def post(self, request, *args, **kwargs):
        items = None
        orders = None
        if request.method == 'POST':
            orders = OrderForm(request.POST, prefix="orders")
            items = OrderItemForm(request.POST, prefix="items")
            if orders.is_valid() and items.is_valid():
                primary = orders.save()
                print("------",primary)

                items.cleaned_data["order"] = primary
                b = items.save(commit=False)
                b.order = primary
                b.save()
                return HttpResponseRedirect(reverse('order:show'))
        


    

class UpdateDataView(SuccessMessageMixin,UpdateView):
    model=OrderItem
    form_class = OrderItemForm
    template_name = "order/update.html"
    success_url ="/order/show/"
    success_message ='order updated  successfully'
    # context_object_name ="items"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = OrderItemForm()
        return context
    

