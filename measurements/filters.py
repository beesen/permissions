import django_filters

from .models import Measurement


class MeasurementFilter(django_filters.FilterSet):
    class Meta:
        model = Measurement
        fields = {
            # 'respondent': ['icontains']
        }
