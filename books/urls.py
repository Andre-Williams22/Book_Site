from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    #book/<int:book_id>
    path('<int:book_id>/', views.detail, name='detail')
]
