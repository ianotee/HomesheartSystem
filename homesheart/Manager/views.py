from django.shortcuts import render


def Manager(request):
    return render(request, 'Manager/home.html')