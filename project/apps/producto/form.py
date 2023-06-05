from dataclasses import field, fields
from django import forms
from .models import Video, Procesador, Mouse

class PlacaForm(forms.ModelForm):
    class Meta:
        model: Video
        fields = ["marca", "modelo", "gama", "precio"]
        