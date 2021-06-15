import re, csv, os

from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from django.contrib.auth.decorators import login_required

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

                return JsonResponse({'done': True})
        else:
            return JsonResponse({'error': 'Please enter a valid email'})

    else:
        return JsonResponse({'error': 'error with http method'})


@login_required
def download(request):
    u = request.user
    if u.username == 'managerJR' or u.username == 'prestMBcom':
        file_path = './listing-beta-utilisateurs.csv'
        with open(file_path, "w") as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['adresses email'])
            for beta_user in BetaUser.objects.all():
                spamwriter.writerow([beta_user.email])
        return FileResponse(
            open(file_path, 'rb'),
            as_attachment=True,
        )