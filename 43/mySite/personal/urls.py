from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('no-edit', views.noEdit),
    path('shop', views.shop)
]