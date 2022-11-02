from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from .filters import SurveyFilter
from .models import Survey
from .tables import SurveyTable


# Create your views here.
class SurveyListView(SingleTableMixin, FilterView):
    model = Survey
    table_class = SurveyTable
    filterset_class = SurveyFilter
