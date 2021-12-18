from django.shortcuts import render
from django.http import JsonResponse
from .models import Post


def create_post(request):
    posts = Post.objects.all()
    response_data = {}

    if request.POST.get('action') == 'post':
        title = request.POST.get('title')
        description = request.POST.get('description')
        author=request.POST.get('author')
        
        response_data['author'] = author
        response_data['title'] = title
        response_data['description'] = description
        
      
        Post.objects.create(
            author=author,
            title = title,
            description = description,
            )
        return JsonResponse(response_data)

    return render(request, 'create_post.html', {'posts':posts})    


# class UpdateCrud(View):
#     def  get(self, request):
#         author1 = request.GET.get('author', None)
#         title1 = request.GET.get('title', None)
#         description1 = request.GET.get('description', None)
       
#         obj = Post.objects.get(id=id)
#         obj.author = author1
#         obj.title = title1
#         obj.description = description1
#         obj.save()

        # user = {'id':obj.id,'author':obj.author,'title':obj.title,'description':obj.description}

        # data = {
        #     'user': user
        # }
        # return JsonResponse(data)


# class DeleteCrud(View):
#     def  get(self, request):
#         id1 = request.GET.get('id', None)
#         Post.objects.get(id=id1).delete()
#         data = {
#             'deleted': True
#         }
#         return JsonResponse(data)