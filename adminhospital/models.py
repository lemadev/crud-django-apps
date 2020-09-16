from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField(max_length=2)
    dni = models.IntegerField(max_length=8)
    def __str__(self):
        return f'{self.lastname}, {self.name}. {self.age}.'

class Medic(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    specialty = models.CharField(max_length=30)
    medic_id = models.IntegerField(max_length=10)
    def __str__(self):
        return f'{self.lastname}, {self.name}. {self.specialty}.'

class Turno(models.Model):
    date = models.DateTimeField()
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    medic = models.ForeignKey('Medic', on_delete=models.CASCADE)
    observations = models.CharField(blank=True, max_length=255)
    def __str__(self):
        return f'{self.date} {self.person} {self.medic}'