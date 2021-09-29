from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

#def index(request):
class PostList(ListView):
    model = Post
    ordering = '-pk'
#    template_name = 'blog/post_list.html'
# post_detail.html

class PostDetail(DetailView):
    model = Post
# post_detail.html

#        posts = Post.objects.all().order_by('-pk')

#        return render (request, 'blog/post_list.html',
#                       {
#                        'posts':posts
#                       }
#                     )

#def single_post_page(request, pk):
 #   post = Post.objects.get(pk=pk)

  #  return render(request, 'blog/post_detail.html',
   #               {
    #                  'post': post
     #             }
      #            )

# Create your views here.
