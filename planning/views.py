from django.http import JsonResponse, FileResponse
from django.views.generic.detail import DetailView
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required

from .models import Planning


class PlanningDetailView(DetailView):
    model = Planning
    template_name = "recipe/detail.html"
