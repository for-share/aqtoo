from django.conf.urls import url, include
from django.contrib import admin

from person_auth import views

urlpatterns = [
    url(r'^reg/', views.reg, name='reg'),
    url(r'^login/', views.login, name="login"),
    url(r'^phone/', views.phone, name="phone"),
]