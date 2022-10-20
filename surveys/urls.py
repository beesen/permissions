from django.urls import path

from . import views

app_name = 'surveys'
urlpatterns = [
    path('', views.SurveyListView.as_view(), name="list"),
    # path('add/', views.SurveyCreateView.as_view(), name="add"),
    # path('<int:pk>/change/', views.SurveyUpdateView.as_view(), name="change"),
    # path('<int:pk>/detail/', views.SurveyDetailView.as_view(), name="detail"),
    # path('<int:pk>/delete/', views.SurveyDeleteView.as_view(), name="delete"),
]
