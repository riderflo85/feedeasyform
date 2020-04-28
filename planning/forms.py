from django import forms
from django.forms import ModelForm
from .models import Recipe, Categorie


class RecipeForm(ModelForm):

    identifiant = forms.CharField(
        initial='recipe',
        widget=forms.TextInput(
            attrs={'class': 'd-none'}
        ),
    )

    class Meta:
        model = Recipe
        fields = ['name', 'prepare_duration', 'cooking_time', 'step', 'food_quantity', 'categorie', 'price_scale', 'level', 'identifiant']


class CategorieForm(ModelForm):

    identifiant = forms.CharField(
        initial='categorie',
        widget=forms.TextInput(
            attrs={'class': 'd-none'}
        ),
    )

    class Meta:
        model = Categorie
        fields = ['name', 'identifiant']
