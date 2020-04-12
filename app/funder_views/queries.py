from django.shortcuts import render, redirect
from app.models import Sponsorship, Sponsor, SponsorSponsorship
from django.db.models import Sum

def queries(request):
    context_dict = {}
    if request.POST:
        try:
            sponsors = Sponsor.objects.all()
            sel_month= request.POST['month']
            sel_quarter= request.POST['quart']
            sel_year= request.POST['Year']

            sponsors.filter(created_at__year=sel_year).aggregate(Yearly=Sum('offer'))
            sponsors.filter(created_at__month=sel_month).aggregate(Monthly=Sum('offer'))
            sponsors.filter(created_at__quarter=sel_quarter).aggregate(Quarterly=Sum('offer'))

            redirect('/')
        except:
            return render(request, 'app/queries.html', context_dict)
    else:
        return render(request, 'app/queries.html', context_dict)
