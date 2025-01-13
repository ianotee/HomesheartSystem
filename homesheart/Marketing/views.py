from django.shortcuts import render


def Marketing(request):
    return render(request, 'Marketing/home.html')
