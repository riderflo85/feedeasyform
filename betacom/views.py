import re

from django.shortcuts import render
from django.http import JsonResponse

from .models import BetaUser


def index(request):
    return render(request, 'betacom/index.html')


def register_beta(request):
    if request.method == 'POST':
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        email_user = request.POST['email']
        if (re.search(regex, email_user)):
            try:
                BetaUser.objects.get(email=email_user)
                return JsonResponse({'error': 'User already exist'})

            except BetaUser.DoesNotExist:
                new_beta = BetaUser()
                new_beta.email = email_user
                new_beta.save()
                # Envoyer un mail de confirmation

                return JsonResponse({'state': 'done'})
        else:
            return JsonResponse({'error': 'Please enter a valid email'})

    else:
        return JsonResponse({'error': 'error with http method'})
