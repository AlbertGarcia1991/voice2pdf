from django import forms
from .models import Voice2Pdf


class PdfForm(forms.ModelForm):
    class Meta:
        model = Voice2Pdf
        fields = "__all__"
