from django.urls import path
from bakery_app import views

urlpatterns = [
   path('', views.home,name='index'),
   path('produtos/', views.produtos, name='produtos'),
]
