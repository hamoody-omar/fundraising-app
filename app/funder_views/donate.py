from django.shortcuts import render

def donation(request):
    context_dict = {}
    return render(request, 'app/donate.html', context_dict)
