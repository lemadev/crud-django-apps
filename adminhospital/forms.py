from django.forms import ModelForm, DateTimeInput, Textarea, TextInput, NumberInput
from adminhospital.models import Turno, Medic, Person

class TurnForm(ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'
        widgets = {
            'date': DateTimeInput(attrs={'type':'date'}),
            'observations': Textarea(attrs={'rows':5, 'cols':50})
        }

class MedicForm(ModelForm):
    class Meta:
        model = Medic
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'maxlength':20, 'required': True}),
            'lastname': TextInput(attrs={'maxlength':20, 'required': True}),
            'specialty': TextInput(attrs={'maxlength':20, 'required': True}),
            'medic_id': NumberInput(attrs={'maxlength':20, 'required': True}),
        }
        
class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'maxlength':20, 'required': True}),
            'lastname': TextInput(attrs={'maxlength':20, 'required': True}),
            'age': NumberInput(attrs={'maxlength':20, 'required': True}),
            'dni': NumberInput(attrs={'maxlength':20, 'required': True}),
        }