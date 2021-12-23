from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='about'),
    path('menu', views.menu, name ='menu'),
    path('Payment', views.pay, name ='pay'),
    path('information_about_project', views.info, name ='info'),
    path('information_about_teammates', views.team, name ='team'),
    path('developers_contacts', views.contacts, name ='contacts'),
    path('adminpanel', views.adminpanel, name='adminpanel'),

    path('/create', views.create, name='create'),
    path('/<int:pk>', views.DishesDetailView.as_view(), name='detail'),
    path('/<int:pk>/update', views.DishesUpdateView.as_view(), name='update'),
    path('/<int:pk>/delete', views.DishesDeleteView.as_view(), name='delete')
]
