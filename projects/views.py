from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from .filters import ProjectFilter
from .models import Project
from .tables import ProjectTable


# Create your views here.
class ProjectListView(SingleTableMixin, FilterView):
    model = Project
    table_class = ProjectTable
    filterset_class = ProjectFilter
