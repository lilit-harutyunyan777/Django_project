"""third_project URL Configuration

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
from django.urls import path, include
from third_app import views
from datetime import datetime

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('', views.null),
    path('font/', views.my_font),
    path('greeting/', views.greeting),
    path('introduction/', views.introduction),
    path('current_date_time/', views.current_datetime),
    path('my_dictionary/', views.my_dictionary),
    path('third_app/', include("third_app.urls")),
]
