from django.http import Http404
from django.shortcuts import render, get_object_or_404
from main import models
def index(request):
    # queries are executed lazily
    latest_articals=models.Article.objects.all().order_by('-createdAt')[0:10]
    context={
        'latest_articals':latest_articals
    }
    return render(request,'main/index.html',context)

def article(request,pk):
    # try:
    #     article=models.Article.objects.get(id=pk)
    # except:
    #     raise Http404()
    article=get_object_or_404(models.Article,pk=pk)
    context={
        'article':article
    }
    return render(request,'main/article.html',context)

def author(request,pk):
    author=get_object_or_404(models.Author,pk=pk)
    context={
        'author':author
    }
    return render(request,'main/author.html',context)

def create_article(request):
    authors = models.Author.objects.all()
    context = {
        'authors': authors
    }
    if request.method=='POST':
        print(request.method)
        if request.method == "POST":
            title = request.POST['title']
        article_data = {
            'title': title,
            'content': request.POST['content'],
        }
        article = models.Article.objects.create(**article_data)
        # method 1 use author list[]
        author = models.Author.objects.get(pk=request.POST['author'])
        article.authors.set([author])
        # method 2 use filter to iteraterable
        # author = models.Author.objects.filter(pk=request.POST['author'])
        # article.authors.set(author)
        context['success']=True

    return render(request,'main/create_article.html',context)

# Create your views here.
