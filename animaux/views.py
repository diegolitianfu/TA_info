
from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.shortcuts import render,get_object_or_404
from .models import Equipement,Animaux
from django.urls import reverse
from django.views import generic

# Create your views here.
def liste_animaux(request):
    animaux = Animaux.objects.all()
    content = {'animaux':animaux}
    return render(request,'animaux/liste.html',content)

def detail(request,animaux_id):
    try:
        animaux = Animaux.objects.get(pk = animaux_id)
    except Animaux.DoesNotExist:
        raise Http404("Animaux dose not exist")
    content = {'animaux':animaux}
    return render(request,'animaux/detail.html',content)
def results(request):
    pass

def nourrir(request,animaux_id):
    try:
        animaux = Animaux.objects.get(pk = animaux_id)
    except Animaux.DoesNotExist:
        raise Http404("Animaux dose not exist")
    equipement = Equipement.objects.get(equipement_name= 'mangeoire')
    if animaux.etat != 'affame':
        return render(request,'animaux/detail.html',{
            'animaux': animaux,
            'error_message':"deole,ce animal n'est pas faim",
        })
    elif equipement.disponibility != 'libre':
        occupant_name=""
        occupant = equipement.cherche_occupant()
        for occu in occupant:
            occupant_name = occu+";"+occupant_name
        return render(request,'animaux/detail.html',{
            'animaux': animaux,
            'error_message':"desole le mangeoire n'est pas libre, il est occupe par: "+occupant_name,
        })
    else:
        animaux.etat = 'repus'
        #modele.change_état(id_animal, 'repus')
        lieu_vacant =animaux.lieu
        animaux.lieu = 'mangeoire'
        equipement_occupe = Equipement.objects.get(equipement_name=lieu_vacant)
        if equipement_occupe.equipement_name != "litiere":
            equipement_occupe.disponibility = "libre"
            equipement_occupe.save()
        equipement.disponibility = "occupe"
        equipement.save()
        animaux.save()
        return render(request,'animaux/detail.html',{
            'animaux':animaux,
            'success':"vous avez resussi a nourrir : "+animaux.animal_name,
        })

def divertir(request,animaux_id):
    try:
        animaux = Animaux.objects.get(pk = animaux_id)
    except Animaux.DoesNotExist:
        raise Http404("Animaux dose not exist")
    try:
        equipement = Equipement.objects.get(equipement_name="roue")
    except Equipement.DoesNotExist:
        raise Http404("roue dose not exist")

    if animaux.etat != 'repus':
        return render(request,'animaux/detail.html',{
            'animaux': animaux,
            'error_message':"desole, "+animaux.animal_name+",  n'est pas en etat de faire du sport",
        })
    elif equipement.disponibility != 'libre':
        occupant_name=""
        occupant = equipement.cherche_occupant()
        for occu in occupant:
            occupant_name = occu+";"+occupant_name
        return render(request,'animaux/detail.html',{
            'animaux': animaux,
            'error_message':"desole le roue n'est pas libre, il est occupe par : "+occupant_name,
        })
    else:
        animaux.etat = 'fatigue'
        #modele.change_état(id_animal, 'repus')
        lieu_vacant =animaux.lieu
        animaux.lieu = 'roue'
        equipement_occupe = Equipement.objects.get(equipement_name=lieu_vacant)
        if equipement_occupe.equipement_name != "litiere":
            equipement_occupe.disponibility = "libre"
            equipement_occupe.save()
        equipement.disponibility = "occupe"
        equipement.save()
        animaux.save()
        return render(request,'animaux/detail.html',{
            'animaux':animaux,
            'success': "vous avez resussi a divertir:  " + animaux.animal_name,
        })

def coucher(request,animaux_id):
    try:
        animaux = Animaux.objects.get(pk = animaux_id)
    except Animaux.DoesNotExist:
        raise Http404("Animaux dose not exist")
    try:
        equipement = Equipement.objects.get(equipement_name="nid")
    except Equipement.DoesNotExist:
        raise Http404("nid dose not exist")
    if animaux.etat != 'fatigue':
        return render(request,'animaux/detail.html',{
            'animaux': animaux,
            'error_message':"deole, "+animaux.animal_name+",  n'est pas fatigue",
        })
    elif equipement.disponibility != 'libre':
        occupant_name=""
        occupant = equipement.cherche_occupant()
        for occu in occupant:
            occupant_name = occu+";"+occupant_name
        return render(request,'animaux/detail.html',{
            'animaux': animaux,
            'error_message':"desole le nid n'est pas libre, il est occupe par : "+occupant_name,
        })
    else:
        animaux.etat = 'endormi'
        #modele.change_état(id_animal, 'repus')
        lieu_vacant =animaux.lieu
        animaux.lieu = 'nid'
        equipement_occupe = Equipement.objects.get(equipement_name=lieu_vacant)
        if equipement_occupe.equipement_name != "litiere":
            equipement_occupe.disponibility = "libre"
            equipement_occupe.save()
        equipement.disponibility = "occupe"
        equipement.save()
        animaux.save()
        return render(request,'animaux/detail.html',{
            'animaux':animaux,
            'success': "vous avez resussi a coucher:  " + animaux.animal_name,
        })

def reveiller(request,animaux_id):
    try:
        animaux = Animaux.objects.get(pk = animaux_id)
    except Animaux.DoesNotExist:
        raise Http404("Animaux dose not exist")
    if animaux.etat != 'endormi':
        return render(request,'animaux/detail.html',{
            'animaux': animaux,
            'error_message':"desole, "+animaux.animal_name+"  ne dort pas ",
        })
    else:
        animaux.etat = 'affame'
        #modele.change_état(id_animal, 'repus')
        lieu_vacant =animaux.lieu
        animaux.lieu = 'litiere'
        equipement_occupe = Equipement.objects.get(equipement_name=lieu_vacant)
        if equipement_occupe.equipement_name != "litiere":
            equipement_occupe.disponibility = "libre"
            equipement_occupe.save()
        animaux.save()
        return render(request,'animaux/detail.html',{
            'animaux':animaux,
            'success': "vous avez resussi a reveiller: " + animaux.animal_name,
        })








