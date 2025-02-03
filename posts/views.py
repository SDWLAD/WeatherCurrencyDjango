from django.shortcuts import render, redirect
from .models import *
from .forms import *

def pages(request):
    articles = Article.objects.order_by('views')
    return render(request, 'posts.html', {"articles":articles})

def page(request, id):
    article = Article.objects.get(pk=id)
    try:request.session[f'{id}']
    except:
        article.views+=1
        request.session[f'{id}'] = True

    article.save()
    comments = Comment.objects.order_by("date")
    if request.method == "POST":
        comment = Comment()
        comment.article_id = id
        comment.text = request.POST["text"]
        comment.save()
    return render(request, "post_detail.html", {'article':article, 'comment':comments})

def create_article_page(request):
    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/posts")
    return render(request, "create-article.html", {"form":form })