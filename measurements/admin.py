from django.contrib import admin

from .models import Measurement


# Register your models here.
class MeasurementAdmin(admin.ModelAdmin):
    model = Measurement
    list_display = (
    "pk", "respondent", "schedule", "begin_dt", "end_dt", "invited_dt", "received_dt",
    "n_invited", "measurement_dt")


admin.site.register(Measurement, MeasurementAdmin)
