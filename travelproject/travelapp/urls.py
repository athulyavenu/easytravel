from django.contrib import admin

from travelproject import settings
from . import views
from django.urls import path


urlpatterns = [

    path('',views.demo,name='demo'),
    # path('add/',views.addition,name='about'),
    # path('contact/',views.contact,name='contact'),
    # path('state/',views.state,name='state')
]

