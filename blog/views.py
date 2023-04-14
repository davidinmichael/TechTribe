from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def blog(request):
    articles = Article.objects.all()
    context = {
        "articles" : articles,
    }
    return render(request, "blog/blog.html", context)
