from django.db import models

# Create your models here.
class Animaux(models.Model):
    animal_name = models.CharField(max_length=50)
    etat = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    race = models.CharField(max_length=50)
    lieu = models.CharField(max_length=50)

    def __str__(self):
        return self.animal_name

    def change_lieu(self, lieu):
        if lieu.disponibility != 'occupé':
            lieu_vacant = self.lieu
            self.lieu = lieu.equipement_name
            if lieu.equipement_name != 'litière':
                 lieu.disponibility = 'occupé'
            equipement = Equipement.objects.filter(equipement_name= lieu_vacant)
            equipement.disponibility = 'libre'


class Equipement(models.Model):
    equipement_name = models.CharField(max_length=50)
    disponibility = models.CharField(max_length=50)

    def __str__(self):
        return self.equipement_name

    def cherche_occupant(self):
        animaux = Animaux.objects.all()
        #equipements = Equipement.objects.all()
      #  if self in equipements:
        liste = []
        for animal in animaux:
            if self.equipement_name == animal.lieu:
                liste += [animal.animal_name]
        return liste
