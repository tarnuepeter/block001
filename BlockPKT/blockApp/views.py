from django.shortcuts import render, get_list_or_404
from .models import *

# Create your views here.
def index(request):
    return render(request, 'blog-app/index.html')

def read_detail(request):
    return render(request, 'blog-app/readmore.html')
