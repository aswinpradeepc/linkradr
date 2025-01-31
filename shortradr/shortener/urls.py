from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('shorten/', shorten_url, name='shorten_url'),
    path('profile/', profile, name='profile'),
    path('<str:short_code>/', redirect_url, name='redirect_url'),
]
