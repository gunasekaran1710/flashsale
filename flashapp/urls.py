from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('flashsales/', views.flashsales_view, name='flashsales'),
]
