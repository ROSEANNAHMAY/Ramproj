"""Ramproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Ramsched import views
from Ramsched.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.ClientPage, name='mainpage'),
    path('service/',views.ServicePage, name='service'),
    path('artist/',views.ArtistPage, name='artist'),

    path('add-client/',views.AddClient, name='add-client'), path('add-artist/',views.AddArtist, name='add-artist'),
    path('add-service/',views.AddService, name='add-service'),
    path('payment/',views.AddPayment, name='payment'),
    path('voucher/',views.AddVoucher, name='voucher'),

    path('update-client/<str:pk>/', views.UpdateClient, name="update-client"),
    path('delete-client/<str:pk>/', views.DeleteClient, name="delete-client"),

    path('update-artist/<str:pk>/', views.UpdateArtist, name="update-artist"),
    path('delete-artist/<str:pk>/', views.DeleteArtist, name="delete-artist"),

    path('update-service/<str:pk>/', views.UpdateService, name="update-service"),
    path('delete-service/<str:pk>/', views.DeleteService, name="delete-service"),

    path('admin/', admin.site.urls),
      ] + static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)


