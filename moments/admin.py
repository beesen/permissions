from django.contrib import admin

from .models import Moment


# Register your models here.
class MomentAdmin(admin.ModelAdmin):
    model = Moment
    list_display = ['project', 'seq_nr', 'nr_of_time_units']


admin.site.register(Moment, MomentAdmin)
