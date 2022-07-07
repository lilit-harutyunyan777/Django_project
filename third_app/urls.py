from django.urls import path
from third_app import views
urlpatterns = [
    path("greeting/", views.greeting),
    path("hello/", views.hello)
]