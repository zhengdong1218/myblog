from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ArticlePost
import markdown
from django.contrib.auth.models import User
from .forms import ArticlePostForm
# Create your views here.
def article_list(request):
    articles=ArticlePost.objects.all()
    context={'articles_list':articles}
    return render(request, 'article/list.html', context)

def article_detail(request,id_detail):
    article=ArticlePost.objects.get(id=id_detail)
    article.body=markdown.markdown(article.body,
                                   extensions=[
                                       'markdown.extensions.extra',
                                       'markdown.extensions.codehilite',
                                   ])
    context={'article_detail':article}
    return render(request,'article/detail.html',context)

def article_create(request):
    if request.method=='POST':
        article_post_form=ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new_article=article_post_form.save(commit=False)
            new_article.author=User.objects.get(id=1)
            new_article.save()
            return redirect('article:article_list_article_urls')
        else:
            return HttpResponse('Invalid data.')
    else:
        article_post_form=ArticlePostForm()
        context={ 'article_post_form': article_post_form }
        return render(request, 'article/create.html', context)

def article_delete(request,id_delete):
    if request.method=='POST':
        article=ArticlePost.objects.get(id=id_delete)
        article.delete()
        return redirect('article:article_list_article_urls')
    else:
        return HttpResponse('POST only')

def article_update(request,id_update):
    article=ArticlePost.objects.get(id=id_update)
    if request.method=='POST':
        article_post_form=ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.title=request.POST['title']
            article.body=request.POST['body']
            article.save()
            return redirect('article:article_detail_article_urls', id_detail=id_update)
        else:
            return HttpResponse('Pls submit again.')
    else:
        article_post_form=ArticlePostForm()
        context={'article_detail':article, 'article_post_form':article_post_form}
        return render(request,'article/update.html',context)

