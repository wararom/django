"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from rent import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.logout,{'template_name': 'registration/logout.html'}),
    path('home/', views.home, name='home'),
    path('create/', views.CreatePersonView.as_view(), name='person'),
    # path('listcar/', views.ListPersonView.as_view(), name='listcar'),
    path('listcar/', views.ListCarView.as_view(), name='car-list'),
    path('rentcar/', views.RentCar.as_view(), name='rent-car'),
    path('success/', views.SuccessRent.as_view(), name='success'),

    #path('login/', auth_views.login, {'template_name': 'core/login.html'}, name='login'),
    #path('logout/', auth_views.logout, name='logout'),
]

