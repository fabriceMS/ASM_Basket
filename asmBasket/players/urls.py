from django.urls import path
from players import views

urlpatterns = [
    
    path('', views.home, name='home_page'),

]