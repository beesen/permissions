from django.contrib import admin

from surveys.models import Survey


# Register your models here.
class SurveyAdmin(admin.ModelAdmin):
    model = Survey
    list_display = ['project', 'survey_type', 'name']


admin.site.register(Survey, SurveyAdmin)