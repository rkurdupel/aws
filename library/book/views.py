from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from order.models import Order
from authentication.models import CustomUser
from django.contrib.auth.decorators import login_required
from .forms import BookForm

def show_books(request):
    filter = None
    if request.method == 'POST':
        filter = request.POST['filter_choise']

    if filter == 'id':
        books = Book.objects.all().order_by(filter)
    elif filter == 'name':
        books = Book.objects.all().order_by(filter)
    elif filter == 'count':
        books = Book.objects.all().order_by(filter)
    else:
        books = Book.objects.all().order_by('id')

    context = {'books': books}
    return render(request, 'book/books.html', context)


def show_book(request, pk):
    book = Book.objects.get(id=pk)

    context = {'book': book}
    return render(request, 'book/book.html', context)


@login_required
def show_specific(request, pk):
    orders = Order.objects.filter(user_id=pk)
    user = get_object_or_404(CustomUser, id=pk)
    books = [order.book for order in orders]

    context = {'books': books, 'user': user}
    return render(request, 'book/specific_user.html', context)

def create_book(request):
    form = BookForm
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    
    context = {'form': form}
    return render(request, 'book/book_form.html', context)

def update_book(request, pk):
    book = Book.objects.get(id = pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')
    
    context = {'form': form}
    return render(request, 'book/book_form.html', context)
