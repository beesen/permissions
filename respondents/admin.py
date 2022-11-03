from django.contrib import admin

from .models import Respondent


# Register your models here.
class RespondentAdmin(admin.ModelAdmin):
    model = Respondent
    list_display = ['name']


admin.site.register(Respondent, RespondentAdmin)
