from django.db import models

from moments.models import Moment
from projects.models import Project
from surveys.models import Survey


# Create your models here.
class Schedule(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    moment = models.ForeignKey(Moment, default=None, on_delete=models.CASCADE)

    class Meta:
        db_table = "schedules"
        ordering = ['project', 'moment', 'survey']

    def __str__(self):
        return f"{self.moment} - {self.survey}"