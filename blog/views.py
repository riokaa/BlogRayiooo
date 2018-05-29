from django.shortcuts import render, render_to_response
from blog.models import Article
from markdown2 import markdown


# Create your views here.
def blog_main(request):
    blog_list = Article.objects.filter(author=1).order_by('-timestamp')
    # 将markdown内容转化为html格式
    for i in blog_list:
        i.content = markdown(i.content, extras=['fenced-code-blocks'], )

    c = {
        'blog_list': blog_list,
    }
    return render_to_response('blog.html', c)


def blog_article(request):
    article_num = request.GET['id']
    article = Article.objects.get(id=article_num)
    # 将markdown内容转化为html格式
    article.content = markdown(article.content, extras=['fenced-code-blocks'], )

    c = {
        'article': article,
    }
    return render_to_response('article.html', c)

