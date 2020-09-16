from django.shortcuts import render, redirect
from adminhospital.models import Medic, Person, Turno
from adminhospital.forms import TurnForm, MedicForm, PersonForm
# Create your views here.

def adminh_index(request):
    turns = Turno.objects.all()
    context = {
        'turns': turns
    }
    return render(request, "turn/index.html", context)

def new_turn(request):
    if request.method == 'POST':
        turnFormPost = TurnForm(request.POST)
        if turnFormPost.is_valid():
            turnFormPost.save()
        return redirect("admin_index")
    turnForm = TurnForm()
    context = {
         'form':turnForm
    }
    return render(request,"turn/turn_new.html", context)

def detail_turn(request, id):
    turn = Turno.objects.get(pk=id)
    context = {
        'turn':turn
    }
    return render(request,"turn/turn_detail.html", context)

def delete_turn(request, id):
    turn = Turno.objects.get(pk=id)
    turn.delete()
    return redirect("admin_index")
    
##Medic
def indexMedics(request):
    medics = Medic.objects.all()
    context = {
        'medics':medics
    }
    return render(request,"medic/indexMedics.html", context)

def edit_medic(request, id):
    medic = Medic.objects.get(pk=id)
    if request.method == 'POST':
        medicFormPost = MedicForm(request.POST, instance=medic)
        if medicFormPost.is_valid():
            medicFormPost.save()
            return redirect("indexMedics")
    medicForm = MedicForm(instance=medic)
    context = {
        'medicForm':medicForm
    }
    return render(request,"medic/new_medic.html", context)

def delete_medic(request, id):
    medic = Medic.objects.get(pk=id)
    medic.delete()
    return redirect("indexMedics")

def new_medic(request):
    if request.method == 'POST':
        medicFormPost = MedicForm(request.POST)
        if medicFormPost.is_valid():
            medicFormPost.save()
        return redirect("indexMedics")
    medicForm = MedicForm()
    context = {
         'medicForm':medicForm
    }
    return render(request,"medic/new_medic.html", context)

##person
def indexPersons(request):
    persons = Person.objects.all()
    context = {
        'persons':persons
    }
    return render(request,"person/indexPerson.html", context)

def edit_person(request, id):
    person = Person.objects.get(pk=id)
    if request.method == 'POST':
        personFormPost = PersonForm(request.POST, instance=person)
        if personFormPost.is_valid():
            personFormPost.save()
            return redirect("indexPersons")
    personForm = PersonForm(instance=person)
    context = {
        'personForm':personForm
    }
    return render(request,"person/new_person.html", context)

def delete_person(request, id):
    person = Person.objects.get(pk=id)
    person.delete()
    return redirect("indexPersons")

def new_person(request):
    if request.method == 'POST':
        personFormPost = PersonForm(request.POST)
        if personFormPost.is_valid():
             personFormPost.save()
        return redirect("indexPersons")
    personForm = PersonForm()
    context = {
         'personForm':personForm
    }
    return render(request,"person/new_person.html", context)