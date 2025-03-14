from django.urls import path
from .views import get_users, create_user, get_users


urlpatterns = [

    path('user/', get_users, name='get_users'),
     path('user/create', create_user, name='create_user'),
]