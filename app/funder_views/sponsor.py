from django.shortcuts import render, redirect
from app.models import Sponsorship, Sponsor, SponsorSponsorship

def sponsor(request):
    context_dict = {}
    if request.POST:
        try:

            if Donation.objects.filter():
                donation = Donation.objects.filter()[0]
            else:
                donation = Donation()
                donation.name = "Corona virus fundraising"
                donation.save()

            donor = Donor()
            donor.full_name = request.POST['firstname'] + " "+ request.POST['lastname']
            donor.amount = request.POST['amount']
            donor.email = request.POST['email']
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
