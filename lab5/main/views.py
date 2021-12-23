from django.shortcuts import render, redirect
from django.views.generic import DeleteView, UpdateView, DetailView

from .forms import DishesForm
from .models import Administator, Dishes, Order, Payment, Waiter, Customer


def menu(request):
    administator = Administator.objects.all()
    dishes = Dishes.objects.all()
    order = Order.objects.all()
    payment = Payment.objects.all()
    waiter = Waiter.objects.all()
    customer = Customer.objects.all()
    return render(request, 'main/menu.html', {
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
            return redirect('http://127.0.0.1:8000/adminpanel')
        else:
            error = 'Форма была неверной'

    form = DishesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/admin_panel.html', data)


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



def index(request):
    return render(request, 'main/Index.html')


def pay(request):
    return render(request, 'main/Payment.html')


def info(request):
    return render(request, 'main/information_about_project.html')


def team(request):
    return render(request, 'main/information_about_teammates.html')


def contacts(request):
    data = {
        'contact1': '+7 702 787 9977',
        'contact2': '+7 708 495 6618',
        'datas': ['Silicon Valley, Google Headquarters', 'akzholbeisenbayev@google.com']
    }
    return render(request, 'main/developers_contacts.html', data)

def adminpanel(request):
    administrator = Administator.objects.all()
    dishes = Dishes.objects.all()
    order = Order.objects.all()
    payment = Payment.objects.all()
    waiter = Waiter.objects.all()
    customer = Customer.objects.all()

    data = {
        'administrator': administrator,
        'dishes': dishes,
        'order': order,
        'payment': payment,
        'waiter': waiter,
        'customer': customer}

    return render(request, 'main/admin_panel.html', data)
