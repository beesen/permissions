from django.contrib import admin

from projects.models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ["name"]


admin.site.register(Project, ProjectAdmin)
