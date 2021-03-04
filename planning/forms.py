from django import forms
from django.forms import ModelForm
from django.utils.functional import lazy

from .models import Planning
from .list_all_models import list_all_planning


class PlanningForm(ModelForm):

    class Meta:
        model = Planning
        fields = '__all__'


class DeletePlanningForm(forms.Form):
    planning = forms.ChoiceField(
        label='Supprimer un planning',
        choices=lazy(list_all_planning, tuple),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    identifiant = forms.CharField(
        initial='planning',
        widget=forms.TextInput(
            attrs={'class': 'd-none'}
        ),
    )
