from django.shortcuts import render, redirect
from app.models import Sponsorship, Sponsor, SponsorSponsorship
from django.db.models import Sum

def queries(request):
    context_dict = {}
    if request.POST:
        sponsors = Sponsor.objects.all()

        reptype= int(request.POST['reptype'])


        

        if reptype==1:
            sel_month= int(request.POST['month'])
            context_dict['result']=sponsors.filter(created_at__month=sel_month).aggregate(Monthly=Sum('offer'))
        elif reptype==2:
            sel_quarter= int(request.POST['quart'])
            context_dict['result']=sponsors.filter(created_at__quarter=sel_quarter).aggregate(Quarterly=Sum('offer'))
        elif reptype==3:
            sel_year= int(request.POST['year'])
            context_dict['result']=sponsors.filter(created_at__year=sel_year).aggregate(Yearly=Sum('offer'))

        return render(request, 'app/queries.html', context_dict)
    else:
        return render(request, 'app/queries.html', context_dict)
