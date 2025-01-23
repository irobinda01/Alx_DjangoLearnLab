from django.shortcuts import render

# Create your views here.
# Groups: Viewers, Editors, Admins
# Permissions: can_view, can_create, can_edit, can_delete
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Article
from .forms import ArticleForm

@permission_required('your_app.can_view', raise_exception=True)
def view_articles(request):
    articles = Article.objects.all()
    return render(request, 'articles/view_articles.html', {'articles': articles})

@permission_required('your_app.can_create', raise_exception=True)
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_articles')
    else:
        form = ArticleForm()
    return render(request, 'articles/create_article.html', {'form': form})

@permission_required('your_app.can_edit', raise_exception=True)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('view_articles')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/edit_article.html', {'form': form, 'article': article})

@permission_required('your_app.can_delete', raise_exception=True)
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('view_articles')
    return render(request, 'articles/delete_article.html', {'article': article})
