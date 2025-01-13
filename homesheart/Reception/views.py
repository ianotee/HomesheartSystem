from django.shortcuts import render

def Reception(request):
    return render(request, 'Reception/home.html')