from django.shortcuts import render, redirect
from django.views.generic import DeleteView, UpdateView, DetailView

from .forms import DishesForm
from .models import Administator, Dishes, Order, Payment, Waiter, Customer


def db_home(request):
    administator = Administator.objects.all()
    # administator = Administator.objects.order_by('name')
    # administator = Administator.objects.order_by('-name')
    # administator = Administator.objects.order_by('name') #[:1] - ограничение исключительно 1 запись

    dishes = Dishes.objects.all()
    order = Order.objects.all()
    payment = Payment.objects.all()
    waiter = Waiter.objects.all()
    customer = Customer.objects.all()

    return render(request, 'db/db_home.html', {
        'administator': administator,
        'dishes': dishes,
        'order': order,
        'payment': payment,
        'waiter': waiter,
        'customer': customer})

def create(request):
    error = ''
    if request.method == 'POST':
        form = DishesForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/db')
        else:
            error = 'Форма была неверной'

    form = DishesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'db/create.html', data)


class DishesDetailView(DetailView):
    model = Dishes
    template_name = 'db/details_view.html'
    context_object_name = 'dishes'


class DishesUpdateView(UpdateView):
    model = Dishes
    template_name = 'db/create.html'

    fields = ['name', 'price', 'ingredients', 'cooking_time']


class DishesDeleteView(DeleteView):
    model = Dishes
    success_url = 'http://127.0.0.1:8000/db'
    template_name = 'db/dishes-delete.html'


