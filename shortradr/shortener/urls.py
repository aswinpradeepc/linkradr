from django.urls import path
from .views import home, shorten_url, redirect_url

urlpatterns = [
    path('', home, name='home'),
    path('shorten/', shorten_url, name='shorten_url'),
    path('<str:short_code>/', redirect_url, name='redirect_url'),
]
