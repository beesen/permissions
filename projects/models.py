from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        ordering = ['name']
        db_table = 'projects'

    def __str__(self):
        return self.name
