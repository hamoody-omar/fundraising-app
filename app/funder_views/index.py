from django.shortcuts import render

def index(request):
    context_dict = {}
    return render(request, 'funder_templates/index.html', context_dict)