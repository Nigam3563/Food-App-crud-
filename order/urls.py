from django.urls import path,include
from .views import OrderFormview
# from .views import OrderItemview
from .views import ShowpageView
from .views import UpdateDataView

app_name="order"
urlpatterns = [
	path('', OrderFormview.as_view()),
    # path('item/', OrderItemview.as_view(),name='items'),
    path('show/', ShowpageView.as_view(),name='show'),
    path('update/<int:pk>', UpdateDataView.as_view(),name="update_detail"),
   
   
]

   

