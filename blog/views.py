from django.shortcuts import render, render_to_response
from blog.models import Article


# Create your views here.
def blog_article(request):
    blog_list = Article.objects.all()
    c = {
        'blog_list': blog_list,
    }
    return render_to_response('article.html', c)

