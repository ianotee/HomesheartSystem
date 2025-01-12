from django.shortcuts import render
from django.contrib.auth.decorators import login_required


#@login_required



def Accounts(request):
    return render(request, 'Accounts/home.html')






