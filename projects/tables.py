import django_tables2 as tables

from projects.models import Project


class ProjectTable(tables.Table):
    class Meta:
        attrs = {"class": "table table-sm table-hover data-table"}
        template_name = "django_tables2/bootstrap4.html"
        model = Project
        fields = ['id', 'name', 'created']