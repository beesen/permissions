from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import QuerySet
from django.views import generic
from django.views.generic import ListView

from surveys.models import Survey


# Create your views here.
class SurveyListView(UserPassesTestMixin, ListView):
    model = Survey
    permission_required = "survey.view_survey"

    def test_func(self):
        j = self.request.user.has_perm("surveys.view_survey")
        return j

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        return queryset
