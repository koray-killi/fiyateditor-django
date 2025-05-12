from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('success/', views.success),
    path('form', views.index_form, name="index_form")
]