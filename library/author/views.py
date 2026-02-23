from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Author
from book.models import Book
from .forms import CreateEditAuthorForm


@login_required
def show_authors(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'author/authors.html', context)


@login_required
def create_author(request):
    context = {}
    books = Book.objects.all()
    form = CreateEditAuthorForm()
   
    context['form'] = form
    if request.method == 'POST':
        form = CreateEditAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors')
    else:
        #context = {'books': books}
        context['books'] = books
        return render(request, 'author/create_author.html', context)

@login_required
def edit_author(request, author_id):
    context = {}
    author = Author.get_by_id(author_id)
    context['author_id'] = author_id

    if request.method == "POST":
        form = CreateEditAuthorForm(request.POST, instance = author)
        if form.is_valid():
            form.save()
            return redirect('authors')
        else:
            return redirect('edit_author')
    else:
        form = CreateEditAuthorForm(instance = author)
        context['form'] = form

        return render(request, "author/edit_author.html", context)
@login_required
def delete_author(request, pk):
    author = Author.objects.filter(id=pk)
    author.delete()
    return redirect('authors')
