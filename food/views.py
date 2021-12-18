from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import admin
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# serve list of all data items the data listview.
class IndexClassView(ListView):
  model=Item
  template_name="food/index.html"
  context_object_name='item_list'

#detailview  
class FoodDetail(DetailView):
  model = Item
  template_name="food/detail.html"

#add details = create view#
class FoodCreate(CreateView):
    model = Item
    template_name='food/item-form.html'
    fields = ['item_name','item_des', 'item_price','item_image']
    def form_valid(self,form):
      form.instance.user_name=self.request.user 
      return super().form_valid(form)
    success_url="/food/"


#update view details = class based view#
class UpdateDetail(UpdateView):
    model = Item
    fields = ['item_name','item_des', 'item_price','item_image']
    template_name='food/item-form.html'
    success_url ="/food/"


#deleteview=classs based view
class DeleteDetail(SuccessMessageMixin,DeleteView):
     model = Item
     template_name='food/item-delete.html'
     success_url ="/food/"
     success_message ="object deleted sucessfully"

     def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteDetail, self).delete(request, *args, **kwargs)
    



