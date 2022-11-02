import django_tables2 as tables

from .models import Survey


class SurveyTable(tables.Table):
    class Meta:
        attrs = {"class": "table table-sm table-hover data-table"}
        template_name = "django_tables2/bootstrap4.html"
        model = Survey
        fields = ['id', 'name', 'survey']