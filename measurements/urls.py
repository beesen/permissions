from django.urls import path

from .views import MeasurementListView, fill_measurements

app_name = 'measurements'
urlpatterns = [
    path('', MeasurementListView.as_view(), name="list"),
    path('fill/', fill_measurements, name="fill"),
]
