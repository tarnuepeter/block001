from django.shortcuts import render, get_list_or_404
from .models import Post

# Create your views here.
def index(request):
    # Trending post
    trendingPost = Post.objects.get(trending=True)
    
    # all non-trending post
    posts = Post.objects.filter(trending=False)

    data_dict = {'trendingPost': trendingPost, 'posts': posts}

    return render(request, 'blog-app/index.html', data_dict)

def read_detail(request, slug):
    post = Post.objects.get(slug=slug)
    comment = Post.comment_set.all()
    context_d = {'post': post, 'comment':comment}
    return render(request, 'blog-app/readmore.html', context_d)
