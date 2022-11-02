from django.contrib import admin

from surveys.models import Survey


# Register your models here.
class SurveyAdmin(admin.ModelAdmin):
    model = Survey
    list_display = ["name", "project"]


admin.site.register(Survey, SurveyAdmin)