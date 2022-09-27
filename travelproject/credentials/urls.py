from django.contrib import admin

from travelproject import settings
from . import views
from django.urls import path


urlpatterns = [

    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    # path('add/',views.addition,name='about'),
    # path('contact/',views.contact,name='contact'),
    # path('state/',views.state,name='state')
]
