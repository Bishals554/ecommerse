from django import views
from django.urls import path
from core.views import index

app_name = 'core'
urlpatterns = [
    path('index/', index),
]