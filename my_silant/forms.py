from django import forms
from .models import *

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = '__all__'
        widgets ={
            'type': forms.RadioSelect()
        }

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = '__all__'