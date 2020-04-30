from django import forms
from django.forms import ModelForm
from django.utils.functional import lazy
from .models import Food, Group
from .list_all_db import list_all_food, list_all_group


class FoodForm(ModelForm):

    identifiant = forms.CharField(
        initial='food',
        widget=forms.TextInput(
            attrs={'class': 'd-none'}
        ),
    )

    class Meta:
        model = Food
        fields = ['name', 'description', 'group', 'identifiant']


class GroupForm(ModelForm):

    identifiant = forms.CharField(
        initial='group',
        widget=forms.TextInput(
            attrs={'class': 'd-none'}
        ),
    )

    class Meta:
        model = Group
        fields = ['name', 'identifiant']


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


class DeleteGroupForm(forms.Form):
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
