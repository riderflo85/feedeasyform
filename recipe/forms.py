from django import forms
from django.forms import ModelForm
from django.utils.functional import lazy

from .models import Recipe, CategorieRecipe, Utensil, OriginRecipe, DietaryPlan
from .list_all_db import list_all_recipe, list_all_categ, list_all_utensil, \
    list_all_origin_recipe, list_all_diet


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
    name = forms.CharField(
        label='Nom de la recette',
        required=True,
        widget=forms.TextInput(
            attrs={'id': 'id_name_recipe'}
        )
    )
    typical_recipe_city = forms.CharField(
        label='Recette typique de la ville de',
        required=False,
        widget=forms.TextInput(
            attrs={'id': 'id_typical_recipe_city'}
        )
    )

    class Meta:
        model = Recipe
        fields = [
            'name',
            'preparation_time',
            'cooking_time',
            'step',
            'tip',
            'portion',
            'point',
            'image',
            'source',
            # 'categorie',
            'origin',
            'typical_recipe_city',
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


class DietaryPlanForm(ModelForm):

    identifiant = forms.CharField(
        initial='diet',
        widget=forms.TextInput(
            attrs={'class': 'd-none'}
        ),
    )

    class Meta:
        model = DietaryPlan
        fields = ['name', 'description', 'identifiant']


class DeleteOriginRecipe(forms.Form):
    origin = forms.ChoiceField(
        label='Supprimer une origine de recette',
        choices=lazy(list_all_origin_recipe, tuple),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    identifiant = forms.CharField(
        initial='origin_recipe',
        widget=forms.TextInput(
            attrs={'class': 'd-none'}
        )
    )


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


class DeleteDietForm(forms.Form):
    diet = forms.ChoiceField(
        label='Supprimer un régime alimentaire',
        choices=lazy(list_all_diet, tuple),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    identifiant = forms.CharField(
        initial='diet',
        widget=forms.TextInput(
                attrs={'class': 'd-none'}
        ),
    )
