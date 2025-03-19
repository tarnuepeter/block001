from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.urls import reverse

from .models import Post 
from .forms import PostForm, CommentForm

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
    comments = post.comment_set.all()
    form = CommentForm()
    new_comment = None 

    if request.method == "POST":
        form = CommentForm(request.POST)
        new_comment = form.save(commit=False)
        new_comment.post = post 
        new_comment.save()
        return HttpResponseRedirect(reverse("read-detail", kwargs={"slug": slug }))
    context_d = {'post': post, 'comments':comments, 'form':form}
    return render(request, 'blog-app/post-detail.html', context_d)
