from django import forms
from .models import deadline

class TeslimForm(forms.ModelForm):
    class Meta:
        model=deadline
        fields=['ogrenci','sinav','dosya']