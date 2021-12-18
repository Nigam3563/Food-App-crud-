from django.shortcuts import render
from django.views.generic import *
from .forms import *
from .models import *
from django.http import JsonResponse
from .models import Fruits




# class Fruitview(CreateView):
#     model=Fruits
#     # form_class = Fruitforms
#     template_name = "Fruit/fruit.html"
#     success_url ="/fruit/"
#     context_object_name="fruit_list"
#     # success_message ='order created successfully'
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context["fruits"] = Fruits.objects.all()
#     #     return context

def create_post(request):
    posts = Fruits.objects.all()
    response_data = {}

    if request.POST.get('action') == 'post':
        title = request.POST.get('fruit_name')
        description = request.POST.get('fruit_price')

        response_data['title'] = title
        response_data['description'] = description

        Fruits.objects.create(
            title = title,
            description = description,
            )
        return JsonResponse(response_data)

    return render(request, 'Fruit/fruit.html', {'posts':posts})        

