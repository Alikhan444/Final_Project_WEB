from .models import Administator, Dishes, Order, Payment, Waiter, Customer

from django.forms import ModelForm, TextInput, NumberInput, Textarea, ImageField


class DishesForm(ModelForm):
    class Meta:
        model = Dishes
        fields = ['name', 'price', 'ingredients', 'cooking_time']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название блюда'
            }),

            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стоимость'
            }),

            "ingredients": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ингредиенты'
            }),

            "cooking_time": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время приготовления'
            })
        }

        # "picture": ImageField
