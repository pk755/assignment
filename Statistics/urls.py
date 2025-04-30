# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('results/', views.results, name='results'),
    path('cart/', views.cart, name='cart'),
    path('clear/', views.clear, name='clear'),

]
