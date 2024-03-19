from django import forms
from .models import Maintenance, Complaint


class BaseForm(forms.ModelForm):
    class Meta:
        abstract = True
        widgets = {
            'type': forms.RadioSelect()
        }


class MaintenanceForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = Maintenance
        fields = '__all__'


class ComplaintForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = Complaint
        fields = '__all__'
