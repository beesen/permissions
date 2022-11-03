from django.db import models

from respondents.models import Respondent
from schedules.models import Schedule


# Create your models here.
class Measurement(models.Model):
    respondent = models.ForeignKey(Respondent, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    begin_dt = models.DateField(null=True, default=None)
    end_dt = models.DateField(null=True, default=None)
    invited_dt = models.DateField(null=True, default=None)
    received_dt = models.DateField(null=True, default=None)
    measurement_dt = models.DateField(null=True, default=None)
    n_invited = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "measurements"
