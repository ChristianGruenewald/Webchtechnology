from django.db import models
from datetime import date

class Bugs(models.Model): 
    kurzbeschreibung=models.CharField(max_length=40, unique=True)
    beschreibung=models.CharField(max_length=200)
    status=models.CharField(max_length=10) # Status ist codiert in: 'N'=neu, O=Offen, I= IN ARBEIT C=Geschlossen, P= BEREIT ZU PRÜFUNG
    prio=models.CharField(max_length=10)
    melder=models.CharField(max_length=40)
    datum=models.DateField(default=date.today)

