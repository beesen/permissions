from django.db import models

from projects.models import Project


# Create your models here.
class Survey(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)

    class Meta:
        ordering = ["name"]
        db_table = "surveys"

    def __str__(self):
        return self.name
