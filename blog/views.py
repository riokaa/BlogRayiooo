from django.shortcuts import render, render_to_response
from blog.models import Article


# Create your views here.
def blog_main(request):
    blog_list = Article.objects.all()
    c = {
        'blog_list': blog_list,
    }
    return render_to_response('blog.html', c)


def blog_article(request):
    article_num = request.GET['article']
    article = Article.objects.get(id=article_num)
    c = {
        'article': article,
    }
    return render_to_response('article.html', c)

