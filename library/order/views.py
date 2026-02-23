from book.models import Book
from .models import Order
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from .forms import OrderForm

@login_required
def create_order(request):
    form = OrderForm
    user = request.user
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
        
            book = form.cleaned_data['book']
            plated_end_at = datetime.now() + timedelta(days=7)
            order = Order.objects.create(
                book = book, user = user, plated_end_at = plated_end_at
            )
            return redirect('orders')
        
    context = {'form': form}
    return render(request, 'order/order_form.html', context)


@login_required
def update_order(request, pk): 
    order = Order.objects.get(id=pk)
    form = OrderForm(instance = order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save() 
            return redirect('orders')
    
    context = {'form': form}
    return render(request, 'order/order_form.html', context)

@login_required
def show_orders(request):
    orders = Order.objects.all()

    context = {'orders': orders}
    return render(request, 'order/orders.html', context)


@login_required
def close_order(request, pk):
    order = Order.objects.filter(id=pk)
    order.delete()
    return redirect('orders')

