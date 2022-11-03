import django_tables2 as tables

from .models import Measurement


class MeasurementTable(tables.Table):
    class Meta:
        attrs = {"class": "table table-sm table-hover data-table"}
        template_name = "django_tables2/bootstrap4.html"
        model = Measurement
        fields = ['id', 'begin_dt', 'end_dt', 'invited_dt', 'received_dt',
                  'measurement_dt', 'n_invited', 'respondent', 'schedule']
