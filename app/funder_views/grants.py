from django.shortcuts import render, redirect
from app.models import Funder

def grant(request):
    context_dict = {}
    if request.POST:
            funds = Funder()
            funds.organization_name=request.POST['name']
            funds.description=request.POST['Description']
            funds.website_url=request.POST['company']
            funds.organization_email_address=request.POST['email']
            funds.organization_phone_number=request.POST['phonenumber']
            funds.save()
            print("******************",funds.organization_name)
            return redirect('/')
    else:
        return render(request, 'app/grants.html', context_dict)




        


