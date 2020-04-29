from django import forms
from django.forms import ModelForm
from .models import Food, Group


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