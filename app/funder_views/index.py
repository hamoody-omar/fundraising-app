from django.shortcuts import render
from app.models import Donor, Donation

def index(request):
    context_dict = {}
    donation = Donation.objects.filter()[0]
    context_dict['campaign_name'] = donation.name
    donors = Donor.objects.filter()
    total = 0
    for donor in donors:
        total += donor.amount
    donation.amount = total
    donation.save()
    context_dict['total'] = total
    return render(request, 'app/index.html', context_dict)
