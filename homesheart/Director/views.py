from django.shortcuts import render

def director(request):
    page ='Directors Dashboard'

    context ={
        'page': page
    }

    return render(request,'director.html',context)
