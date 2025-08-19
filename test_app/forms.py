from django import forms
from .models import Paragraph

class ParagraphForm(forms.ModelForm):
    class Meta:
        model = Paragraph
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5, 'cols': 40, 'placeholder': 'Enter your paragraph here...'})
        }
