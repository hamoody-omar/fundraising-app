from django.shortcuts import render, redirect
from app.models import Sponsorship, Sponsor, SponsorSponsorship

def sponsor(request):
    context_dict = {}
    if request.POST:
        try:

            if Sponsorship.objects.filter():
                donation = Sponsorship.objects.filter()[0]
            else:
                donation = Sponsorship()
                donation.name = "Corona virus fundraising"
                donation.save()

            donor = Sponsor()
            donor.company_name = request.POST['firstname'] + " "+ request.POST['lastname']
            donor.offer = request.POST['amount']
            donor.business_email_address = request.POST['email']
            donor.phone_number = request.POST['phonenumber']
            donor.save()

            donorDonation = DonorDonation()
            donorDonation.donation = donation
            donorDonation.donor = donor

            return redirect('/')
        except:
            render(request, 'app/donate.html', context_dict)
    else:
        return render(request, 'app/donate.html', context_dict)
