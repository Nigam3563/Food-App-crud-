from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from django.contrib.auth import views as authentication_views
from django.conf import settings
from django.conf.urls.static import static
from blog.views import create_post
from movieapp import views
from movieapp.views import MovieListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/',include('food.urls',namespace="food")),
    path('register/',user_views.register,name='register'),
    path('login/',authentication_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',user_views.profilepage,name='profile'),
    path('order/',include('order.urls',namespace="order")),
    path('fruit/',include('Fruit.urls',namespace="fruit")),
    path('blog/', create_post, name="create"),
    # path('movie/', views.movie_list, name="movie"), 
    path('movie/', MovieListView.as_view(),name='movie'),
 
   
]

urlpatterns+=[

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)