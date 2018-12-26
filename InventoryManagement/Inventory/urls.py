
from django.urls import path

from .views import *

urlpatterns = [

    path('api/login', login),
    path('api/addUser', user)

]