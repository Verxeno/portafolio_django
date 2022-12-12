from django import forms
from .models import Portafolio

class PortaForm(forms.ModelForm):
    class Meta:
        model = Portafolio
        fields ='__all__'