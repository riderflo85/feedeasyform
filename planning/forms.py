from django import forms
from django.forms import ModelForm, widgets
from django.utils.functional import lazy

from .models import Recipe, CategorieRecipe, Utensil, OriginRecipe
from .list_all_db import list_all_recipe, list_all_categ, list_all_utensil
from .validator import validate_utensils


# class FoodQuantityForm(ModelForm):

#     identifiant = forms.CharField(
#         initial='food_quantity',
#         widget=forms.TextInput(
#             attrs={'class': 'd-none'}
#         ),
#     )

#     class Meta:
#         model = FoodQuantity
#         fields = ['food', 'quantity', 'identifiant']

class OriginRecipeForm(ModelForm):

    identifiant = forms.CharField(
        initial='origin_recipe',
        widget=forms.TextInput(
            attrs={'class': 'd-none'}
        ),
    )

    class Meta:
        model = OriginRecipe
        fields = [
            'name',
            'identifiant'
        ]


class RecipeForm(ModelForm):

    identifiant = forms.CharField(
        initial='recipe',
        widget=forms.TextInput(
            attrs={
                'class': 'd-none',
                'id': 'id_identifiant_recipe'
            }
        ),
    )

    name_recipe = forms.CharField(
        label='Nom de la recette',
        required=True,
        widget=forms.TextInput(
            attrs={'id': 'id_name_recipe'}
        )
    )

    class Meta:
        model = Recipe
        fields = [
            'name_recipe',
            'preparation_time',
            'cooking_time',
            'step',
            'portion',
            'point',
            'categorie',
            'origin',
            'price_scale',
            'level',
            'identifiant',
        ]


class CategorieRecipeForm(ModelForm):

    identifiant = forms.CharField(
        initial='categorie_recipe',
        widget=forms.TextInput(
            attrs={'class': 'd-none'}
        ),
    )

    class Meta:
        model = CategorieRecipe
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
