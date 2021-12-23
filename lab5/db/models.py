from django.conf import settings
from django.db import models
from django.utils import timezone


class Administator(models.Model):
    name = models.CharField("Имя", max_length=50)
    login = models.CharField("Логин", max_length=50)
    password = models.TextField("Пароль")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = "Администратор"
        verbose_name_plural = "Администраторы"


class Dishes(models.Model):
    name = models.CharField("Имя", max_length=50)
    price = models.IntegerField("Стоимость")
    ingredients = models.TextField("Пароль")
    cooking_time = models.IntegerField("Стоимость")
    picture = models.ImageField("Изображение")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/db/{self.id}'

    class Meta:
        verbose_name = "Блюда"
        verbose_name_plural = "Блюда"


class Order(models.Model):
    type = models.CharField("Вид заказа", max_length=50)
    price = models.IntegerField("Стоимость")
    dishes = models.ForeignKey(Dishes, on_delete=models.CASCADE,)

    # dishes = models.ManyToManyField(Dishes, verbose_name="Блюда", related_name="dishes_name")

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Payment(models.Model):
    price = models.IntegerField("Стоимость")
    type = models.CharField("Способ оплаты", max_length=50)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"


class Waiter(models.Model):
    name = models.CharField("Имя", max_length=50)
    phone = models.CharField("Номер телефона", max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = "Официант"
        verbose_name_plural = "Официанты"


class Customer(models.Model):
    name = models.CharField("Имя", max_length=50)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,)
    # order = models.ManyToManyField(Order, verbose_name="Заказ", related_name="order_name")
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE,)
    # payment = models.ManyToManyField(Payment, verbose_name="Оплата", related_name="payment_type")

    waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE,)

    # waiter = models.ManyToManyField(Waiter, verbose_name="Официант", related_name="waiter_name")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = "Заказщик"
        verbose_name_plural = "Заказщики"
