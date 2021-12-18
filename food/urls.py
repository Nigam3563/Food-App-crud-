from django.urls import path
from . import views

app_name='food'
urlpatterns = [
    path('',views.IndexClassView.as_view(),name='index'), 
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    #add item
    path('add',views.FoodCreate.as_view(),name='create_item'),
    
    # add item
    # path('update/<int:id>/',views.update_item,name='update_item'),
    
    #delete item
    
    path('<int:pk>/delete',views.DeleteDetail.as_view(),name='delete_item'),
    
    #update item
    path('<pk>/update',views.UpdateDetail.as_view(),name='update_detail'),
]   