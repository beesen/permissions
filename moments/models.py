from django.db import models

from projects.models import Project


# Create your models here.
class Moment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    seq_nr = models.PositiveIntegerField()
    nr_of_time_units = models.PositiveIntegerField()

    class Meta:
        db_table = 'moments'
        ordering = ['project', 'seq_nr']

    def __str__(self):
        return f"{self.project} {self.seq_nr}-{self.nr_of_time_units}"
