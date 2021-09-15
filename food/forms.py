from django import forms
from django.forms import ModelForm
from django.utils.functional import lazy
from .models import Food, FoodGroup, StoreRack
from .list_all_db import list_all_food, list_all_group, list_all_racks


class FoodForm(ModelForm):

    identifiant = forms.CharField(
        initial='food',
        widget=forms.TextInput(
            attrs={'class': 'd-none'}
        ),
    )

    class Meta:
        model = Food
        fields = '__all__'


class FoodGroupForm(ModelForm):

    identifiant = forms.CharField(
        initial='food_group',
        widget=forms.TextInput(
            attrs={'class': 'd-none'}
        ),
    )

    class Meta:
        model = FoodGroup
        fields = ['name', 'identifiant']


class StoreRackForm(ModelForm):

    class Meta:
        model = StoreRack
        fields = '__all__'


class DeleteFoodForm(forms.Form):
    food = forms.ChoiceField(
        label='Supprimer un aliment',
        choices=lazy(list_all_food, tuple),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    identifiant = forms.CharField(
        initial='food',
        widget=forms.TextInput(
                attrs={'class': 'd-none'}
        ),
    )


class DeleteFoodGroupForm(forms.Form):
    group = forms.ChoiceField(
        label="Supprimer un groupe d'aliment",
        choices=lazy(list_all_group, tuple),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    identifiant = forms.CharField(
        initial='group',
        widget=forms.TextInput(
                attrs={'class': 'd-none'}
        ),
    )


class DeleteStoreRackForm(forms.Form):
    rack = forms.ChoiceField(
        label="Supprimer un rayon de magasin",
        choices=lazy(list_all_racks, tuple),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    identifiant = forms.CharField(
        initial='store_rack',
        widget=forms.TextInput(
                attrs={'class': 'd-none'}
        ),
    )
