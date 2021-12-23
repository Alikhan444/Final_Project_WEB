from django.contrib import admin
from .models import Administator, Dishes, Order, Payment, Waiter, Customer


admin.site.register(Administator)
admin.site.register(Dishes)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Waiter)
admin.site.register(Customer)