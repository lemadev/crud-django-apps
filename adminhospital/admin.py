from django.contrib import admin
from adminhospital.models import Medic, Person, Turno
# Register your models here.
admin.site.register(Turno)
admin.site.register(Medic)
admin.site.register(Person)

