from django.db import models

# Create your models here.


class TestQuery(models.Model):
    State = models.CharField(max_length=200)
    ProblemID = models.IntegerField(default=0)
    ProblemTitle = models.CharField(max_length=200)
    MobileNubers = models.CharField(max_length=200)
