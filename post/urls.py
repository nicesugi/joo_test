from django.contrib import admin
from django.urls import path
from post import views

urlpatterns = [
    path('', views.PostView.as_view()),
    path('<obj_id>/', views.PostView.as_view()),
]