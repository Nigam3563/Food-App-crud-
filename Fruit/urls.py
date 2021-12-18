from django.urls import path,include

from users import views
from . import views

app_name = 'Fruit'
urlpatterns = [
   path('',views.create_post ,name='post')
#    path('',Fruitview.as_view(), name='crud_ajax'),
#    path('', Fruitview.as_view()),
]