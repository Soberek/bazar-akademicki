from django import forms
from django.forms import inlineformset_factory
from .models import Listing, ListingImage


class ListingForm(forms.ModelForm):
    """Formularz dodawania/edycji oferty."""
    
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'category', 'condition', 'location', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent',
                'placeholder': 'Tytuł oferty'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent',
                'rows': 5,
                'placeholder': 'Opis produktu'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent',
                'placeholder': 'Cena (PLN)',
                'step': '0.01',
                'min': '0'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent'
            }),
            'condition': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent'
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent',
                'placeholder': 'Lokalizacja (np. Warszawa, Mokotów)'
            }),
            'status': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent'
            }),
        }


class ListingImageForm(forms.ModelForm):
    """Formularz dla zdjęć oferty."""
    
    class Meta:
        model = ListingImage
        fields = ['image', 'is_main']
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg',
                'accept': 'image/*'
            }),
            'is_main': forms.CheckboxInput(attrs={
                'class': 'rounded border-gray-300 text-indigo-600 focus:ring-indigo-500'
            }),
        }


# Formset dla wielu zdjęć
ListingImageFormSet = inlineformset_factory(
    Listing,
    ListingImage,
    form=ListingImageForm,
    extra=3,
    max_num=5,
    can_delete=True
)
