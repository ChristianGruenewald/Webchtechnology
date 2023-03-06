#***********************************************************
#************** DATEIHEADER ********************************
#************** Datei:                  views.py    ********
#************** Projekt:                MyBugTracker    ****    
#************** Datum Letzter Änderung: 2023-03-05  ********
#***********************************************************
from django.http import HttpResponseRedirect # Funktion um auf andere URL zu umzuleiten
from django.shortcuts import render # Funktion um HTML dokument auszuwerten und darzustellen
from .models import Bugs # ORM Modell für Bugs

# Indexseite:
def index(request, Changed=2, Delete=False):
    # Changed (int): 0-> Bug Änderung Fehlgeschlagen  1-> Bug Änderung Erfolgreich, 2-> Keine Änderung (standard wert)
    # Delete (bool): False (standardwert), keine Löschung, True: Löschung von Bug erolgreich
    # Darstellung als Alter in Bootstrab (If abfrage in HTML index)
    allBugs=Bugs.objects.all() # Alle Bugs aus Relation Bugs in DB
    return render(request, "index.html", {'allBugs':allBugs, 'Changed':Changed, 'Delete':Delete})

def EnterNewBug(request):
    return render(request, "NewBug.html", {}) # Neuen Bug hinzufügen Frontend

def addNewBug(request):
    # Ergebnisse auf HTML Formulare (per HTML ID):
    titel = request.POST['kurzbeschreibung'] 
    description=request.POST['beschreibung']
    Melder=request.POST['Name']
    Prio=request.POST['PrioRadio']
    new_bug = Bugs(kurzbeschreibung=titel, beschreibung=description, melder=Melder, prio=Prio, status='Offen') # Erzeuge neues Objekt
    new_bug.save() # Speicher neues Objekt in Relation
    return HttpResponseRedirect('/Buglist/index') # Gehe danach wieder auf Index Seite

def ChangeBug(request):
    # Aufruf um Bug zu verändern. Um Formular ausgefüllt darzustellen 
    # Per HTTP GET
    ID=request.GET['id']
    selcted_Bug=Bugs.objects.get(id=ID) # Hole Bug mit gewählter ID 
    Prio=selcted_Bug.prio # Hole Prio aus Objekt 
    PrioHigh=""
    PrioMid=""
    PrioLow=""
    # Prüfe welche Prio Gesetzt ist und speichere in jeweilige Variable
    if Prio=="Hoch":
        PrioHigh="Checked"
    elif Prio=="Mittel":
        PrioMid="Checked"
    else:
        PrioLow="Checked"
    # selected_Bug enhält ganzes Objekt auf Relation
    # PrioHigh, PrioMid, PrioLow enthalten Prio ergebnise aus If abfrage um Radio Button auf checked zu setzen.
    return render(request, "Bug.html", {'SelctedBug':selcted_Bug, 'PrioHigh':PrioHigh, 'PrioMid':PrioMid, 'PrioLow':PrioLow})

def ProcessChangedBug(request):
    id=request.GET['id']
    oldBug=Bugs.objects.get(id=id)
    neueKurzbeschreibung=request.POST['kurzbeschreibung']
    neueBeschreibung=request.POST['beschreibung']
    neuePrio=request.POST['PrioRadio']
    neueStatus=request.POST['State']
    neuerName=request.POST['Name']
    # Testen ob sich was geändert hat:
    if(oldBug.kurzbeschreibung!=neueKurzbeschreibung or oldBug.beschreibung!=neueBeschreibung or oldBug.prio!=neuePrio or oldBug.melder!=neuerName or oldBug.status!=neueStatus):
        # Überprüfung was sich geändert hat
        # in C / PHP wäre dies ein Switch Case
        # Python hat aber kein Switch, deshalb if:
        if(oldBug.beschreibung!=neueBeschreibung):
            oldBug.beschreibung=neueBeschreibung
        if(oldBug.kurzbeschreibung!=neueKurzbeschreibung):
            oldBug.kurzbeschreibung=neueKurzbeschreibung
        if(oldBug.prio!=neuePrio):
            oldBug.prio=neuePrio
        if(oldBug.melder!=neuerName):
            oldBug.melder=neuerName
        if(oldBug.status!=neueStatus):
            oldBug.status=neueStatus
        oldBug.save()
        return index(request, 1)
    else:
        return index(request, 0)

def DeleteBug(request):
    # Funktion um Bug aus DB zu entfernen
    # ID per HTTP GET:
    id=request.GET['id']
    BugToDelete=Bugs.objects.get(id=id) # Filter Bug mit entsprechender ID und speicher diese im Objekt BugToDelete
    BugToDelete.delete() # Lösche gewählten Bug
    return index(request,Delete=True) # gebe Index HTML aus und überschreibe Delete auf True (standard, False,)
      