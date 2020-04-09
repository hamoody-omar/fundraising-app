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
<<<<<<< HEAD
    donation.goal=1000000
=======
    donation.goal=250000
>>>>>>> 24ffefc212b82b717850f95454c45ce5c5b99a65
    donation.save()
    context_dict['goal']=donation.goal
    context_dict['total'] = total
    context_dict['percent']=round(total/donation.goal*100)
    return render(request, 'app/index.html', context_dict)
