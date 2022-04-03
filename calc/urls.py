from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('book/', views.book, name="book"),
    path('Menu/', views.menu, name="Menu"),
    path('Gallery/', views.gallery, name="Gallery"),

]