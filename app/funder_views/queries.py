from django.shortcuts import render, redirect
from app.models import Sponsorship, Sponsor, SponsorSponsorship
from django.db.models import Sum

def queries(request):
    context_dict = {}
    if request.POST:
        try:
            sponsors = Sponsor.object.all()

            reptype= request.POST['reptype']
            sel_month= request.POST['month']
            sel_quarter= request.POST['quart']
            sel_year= request.POST['year']

            print(sponsors.filter(created_at__year=sel_year).aggregate(Yearly=Sum('offer')))

            return redirect('/')
        except:
            return render(request, 'app/queries.html', context_dict)
    else:
        return render(request, 'app/queries.html', context_dict)
