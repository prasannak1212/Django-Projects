from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('animal_info/<int:pk>', views.animal_info ,name='animal_info'),
]