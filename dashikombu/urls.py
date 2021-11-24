from django.urls import path

from . import views

app_name = 'dashikombu'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashiboard', views.DashiBoard, name = 'DashiBoard'),
]