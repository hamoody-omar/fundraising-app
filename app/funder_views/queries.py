from django.shortcuts import render, redirect
from app.models import Sponsor, Donor
from django.db.models import Sum

def queries(request):
    context_dict = {}
    if request.POST:
        which= int(request.POST['whichrec'])
        reptype= int(request.POST['reptype'])

        if which==1:
            sponsors= Donor.objects.all()
            if reptype==1:
                sel_month= int(request.POST['month'])
                context_dict['result']=sponsors.filter(created_at__month=sel_month).aggregate(Monthly=Sum('amount'))
            elif reptype==2:
                sel_quarter= int(request.POST['quart'])
                context_dict['result']=sponsors.filter(created_at__quarter=sel_quarter).aggregate(Quarterly=Sum('amount'))
            elif reptype==3:
                sel_year= int(request.POST['year'])
                context_dict['result']=sponsors.filter(created_at__year=sel_year).aggregate(Yearly=Sum('amount'))
        if which==2:
            sponsors= Sponsor.objects.all()
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
