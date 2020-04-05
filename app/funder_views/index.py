from django.shortcuts import render

def index(request):
    context_dict = {}
    return render(request, 'app/index.html', context_dict)
