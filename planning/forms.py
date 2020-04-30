from django import forms
from django.forms import ModelForm
from django.utils.functional import lazy
from .models import Recipe, Categorie, Utensil, FoodQuantity
from .list_all_db import list_all_recipe, list_all_categ, list_all_utensil


class FoodQuantityForm(ModelForm):

    identifiant = forms.CharField(
        initial='food_quantity',
        widget=forms.TextInput(
            attrs={'class': 'd-none'}
        ),
    )

    class Meta:
        model = FoodQuantity
        fields = ['food', 'quantity', 'identifiant']

class RecipeForm(ModelForm):

    identifiant = forms.CharField(
        initial='recipe',
        widget=forms.TextInput(
            attrs={'class': 'd-none'}
        ),
    )

    class Meta:
        model = Recipe
        fields = [
            'name',
            'prepare_duration',
            'cooking_time',
            'step',
            'food_quantity',
            'categorie',
            'price_scale',
            'level',
            'utensil',
            'identifiant',
        ]


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


class UtensilForm(ModelForm):

    identifiant = forms.CharField(
        initial='utensil',
        widget=forms.TextInput(
            attrs={'class': 'd-none'}
        ),
    )

    class Meta:
        model = Utensil
        fields = ['name', 'identifiant']


class DeleteRecipeForm(forms.Form):
    recipe = forms.ChoiceField(
        label='Supprimer une recette',
        choices=lazy(list_all_recipe, tuple),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    identifiant = forms.CharField(
        initial='recipe',
        widget=forms.TextInput(
            attrs={'class': 'd-none'}
        ),
    )


class DeleteCategForm(forms.Form):
    categ = forms.ChoiceField(
        label='Supprimer une categorie de recette',
        choices=lazy(list_all_categ, tuple),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    identifiant = forms.CharField(
        initial='categ',
        widget=forms.TextInput(
            attrs={'class': 'd-none'}
        ),
    )


class DeleteUtensilForm(forms.Form):
    utensil = forms.ChoiceField(
        label='Supprimer un ustensile de cuisine',
        choices=lazy(list_all_utensil, tuple),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    identifiant = forms.CharField(
        initial='utensil',
        widget=forms.TextInput(
                attrs={'class': 'd-none'}
        ),
    )
