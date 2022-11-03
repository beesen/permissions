from django.http import HttpResponseRedirect
from django.urls import reverse
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from projects.models import Project
from respondents.models import Respondent
from schedules.models import Schedule
from .filters import MeasurementFilter
from .models import Measurement
from .tables import MeasurementTable


# Create your views here.
class MeasurementListView(SingleTableMixin, FilterView):
    model = Measurement
    table_class = MeasurementTable
    filterset_class = MeasurementFilter

def fill_measurements(request):
    # Verwijder alle measurements van Thoresci
    project = Project.objects.get(name='THORESCI')
    measurements = Measurement.objects.all().delete()

    respondents = Respondent.objects.all()
    schedules = Schedule.objects.filter(project=project)
    # Maak nieuwe measurements voor alle respondenten van Thoresci
    for respondent in respondents:
        for schedule in schedules:
            measurement = Measurement(respondent=respondent, schedule=schedule)
            measurement.save()
    return HttpResponseRedirect(reverse('measurements:list'))
