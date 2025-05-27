from django import forms
from .models import Contacts
import re

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'id': 'name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
                'id': 'email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
                'type': 'tel',
                'id': 'phone'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Message',
                'style': 'height: 12rem',
                'id': 'message'
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        pattern = r'^\+?[\d\-]{10,20}$'

        if not re.match(pattern, phone):
            raise forms.ValidationError("Enter a valid phone number.")
        return phone

