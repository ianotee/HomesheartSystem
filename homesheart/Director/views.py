from django.shortcuts import render

def Director(request):

    return render(request, 'Director/home.html')
