from django.db import models


# Create your models here.
class Respondent(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = "respondents"

    def __str__(self):
        return self.name
