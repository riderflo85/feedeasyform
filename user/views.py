from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def task(request):
    return render(request, 'user/task.html')
