import django_filters

from surveys.models import Survey
from .models import Measurement


class MeasurementFilter(django_filters.FilterSet):
    schedule = django_filters.CharFilter(
        field_name='schedule__survey__survey_type',
        label="Survey type contains", lookup_expr='icontains')
    # survey = django_filters.ModelChoiceFilter(
    #     queryset=Survey.objects.all(),
    # )
    survey = django_filters.ChoiceFilter(
        field_name='schedule__survey__survey_type',
        label="Survey",
    )
    class Meta:
        model = Measurement
        fields = {
            # 'respondent': ['icontains']
        }
