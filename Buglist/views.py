from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import Bugs

# Create your views here.
def index(request, Changed=2, Delete=False):
    allBugs=Bugs.objects.all()
    return render(request, "index.html", {'allBugs':allBugs, 'Changed':Changed, 'Delete':Delete})

def EnterNewBug(request):
    return render(request, "NewBug.html", {})

def addNewBug(request):
    titel = request.POST['kurzbeschreibung']
    description=request.POST['beschreibung']
    Melder=request.POST['Name']
    Prio=request.POST['PrioRadio']
    new_bug = Bugs(kurzbeschreibung=titel, beschreibung=description, melder=Melder, prio=Prio, status='Offen')
    new_bug.save()
    return HttpResponseRedirect('/Buglist/index') 

def ChangeBug(request):
    ID=request.GET['id']
    selcted_Bug=Bugs.objects.get(id=ID)
    Prio=selcted_Bug.prio
    PrioHigh=""
    PrioMid=""
    PrioLow=""
    if Prio=="Hoch":
        PrioHigh="Checked"
    elif Prio=="Mittel":
        PrioMid="Checked"
    else:
        PrioLow="Checked"
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
        # Eine Änderung wurde erkannt.
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
    id=request.GET['id']
    
    BugToDelete=Bugs.objects.get(id=id)
    BugToDelete.delete()
    return index(request,Delete=True)
    #return HttpResponseRedirect('/Buglist/index?')  