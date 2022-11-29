from django.contrib.auth.models import Group
from django.views.generic import ListView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin, SingleTableView

from .filters import SurveyFilter
from .models import Survey
from .tables import SurveyTable


# Create your views here.
class SurveyListView(SingleTableMixin, FilterView):
    model = Survey
    table_class = SurveyTable
    filterset_class = SurveyFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        g = Group.objects.get(id=1)
        j = 1
        return context
