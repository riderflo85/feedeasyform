import re, csv

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
        if request.POST['acceptTerm'] == 'true':
            accept = True
        else:
            accept = False
        if (re.search(regex, email_user)):
            try:
                BetaUser.objects.get(email=email_user)
                return JsonResponse({'error': 'User already exist'})

            except BetaUser.DoesNotExist:
                new_beta = BetaUser()
                new_beta.email = email_user
                new_beta.accept_term = accept
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
            fieldnames = ['Adresse e-mail', 'Accepte de recevoir des e-mails']
            spamwriter = csv.DictWriter(csvfile, fieldnames)
            spamwriter.writeheader()
            for beta_user in BetaUser.objects.all():
                if beta_user.accept_term:
                    y_n = 'oui'
                else:
                    y_n = 'non'
                spamwriter.writerow({
                    'Adresse e-mail': beta_user.email,
                    'Accepte de recevoir des e-mails': y_n
                })
        return FileResponse(
            open(file_path, 'rb'),
            as_attachment=True,
        )