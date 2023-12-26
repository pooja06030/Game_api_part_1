from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include
from storefront.views import test


urlpatterns = [
    path('sf/',test),
]
