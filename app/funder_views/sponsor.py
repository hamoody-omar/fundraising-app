from django.shortcuts import render, redirect
from app.models import Sponsorship, Sponsor, SponsorSponsorship

def sponsor(request):
    context_dict = {}
    if request.POST:
        try:

            if Sponsorship.objects.filter():
                sponsorship = Sponsorship.objects.filter()[0]
            else:
                sponsorship = Sponsorship()
                sponsorship.name = "Corona virus sponsorship"
                sponsorship.save()

            sponsor = Sponsor()
            sponsor.company_name = request.POST['firstname'] + " "+ request.POST['lastname']
            sponsor.offer = request.POST['amount']
            sponsor.business_email_address = request.POST['email']
            sponsor.business_phone_number = request.POST['phonenumber']
            sponsor.save()

            sponsorSponsorship = SponsorSponsorship()
            sponsorSponsorship.sponsorship = sponsorship
            sponsorSponsorship.sponsor = sponsor

            return redirect('/')
        except:
            render(request, 'app/sponsor.html', context_dict)
    else:
        return render(request, 'app/sponsor.html', context_dict)
