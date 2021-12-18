from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator
from django.views.generic import ListView
from .filters import MoviesFilter


# Create your views here.

# def movie_list(request):
#     ml=Movies.objects.all()
#     return render(request, 'movieapp/movie_list.html',{'ml':ml})




class MovieListView(ListView):
    paginate_by = 3
    model = Movies
    template_name = 'movieapp/movie_list.html'
    success_url = 'movieapp/movie_list'
    context_object_name = 'movie_list'

#post method apply here
    def post(self, request, *args, **kwargs):
        query=request.POST['movie_name']
        # print("--------",query)
        context=dict()
        context['movie_list'] = Movies.objects.filter(name__icontains=query)
        return render(request, self.template_name,context)

    


# def search(request):
#     user_list = Movies.objects.all()
#     user_filter = MoviesFilter(request.GET, queryset=user_list)
#     return render(request, 'moviesapp/mlist.html', {'filter': user_filter})
   