from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.home_view, name="home"),
    path('superuser/', views.superuser_toggle_view, name="superuser-toggle"),
]
