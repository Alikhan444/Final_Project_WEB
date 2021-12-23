from django.urls import path
from . import views

urlpatterns = [
    path('', views.db_home, name='db_home'),
    path('/create', views.create, name='create'),
    path('/<int:pk>', views.DishesDetailView.as_view(), name='detail'),
    path('/<int:pk>/update', views.DishesUpdateView.as_view(), name='update'),
    path('/<int:pk>/delete', views.DishesDeleteView.as_view(), name='delete')
]