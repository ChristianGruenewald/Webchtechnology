from django.db import models
from datetime import date

class Bugs(models.Model): 
    kurzbeschreibung=models.CharField(max_length=40, unique=True)
    beschreibung=models.CharField(max_length=200)
    status=models.CharField(max_length=15)
    prio=models.CharField(max_length=15)
    melder=models.CharField(max_length=40)
    datum=models.DateField(default=date.today)

    def __str__(self):
        return self.melder+" "+self.status

