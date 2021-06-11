from django.shortcuts import render

# Create your views here.
def register_beta(request):
    return render(request, 'betacom/index.html')