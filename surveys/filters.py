import django_filters

from .models import Survey


class SurveyFilter(django_filters.FilterSet):
    class Meta:
        model = Survey
        fields = {
            'name': ['icontains']
        }
