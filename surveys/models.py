from django.db import models

from projects.models import Project


# Create your models here.
class Survey(models.Model):
    SURVEY_TYPE_CHOICES = (
        ('CRF', 'CRF'),
        ('QST', 'QST')
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    survey_type = models.CharField(max_length=25, choices=SURVEY_TYPE_CHOICES)

    class Meta:
        ordering = ['project', 'survey_type', 'name']
        db_table = 'surveys'

    def __str__(self):
        return f"{self.name} / {self.survey_type}"
