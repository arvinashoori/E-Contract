from django.urls import path
from . import views

urlpatterns = [
    path('send_request/', views.send_request, name='send_request'),
    path('success/', views.success, name='success'),
]