from django.contrib import admin
from .models import Donation, Donor, DonorDonation, Funder

from .models import Donation, Donor, DonorDonation
from .models import Sponsorship, Sponsor, SponsorSponsorship

admin.site.register(Donation)
admin.site.register(Donor)
admin.site.register(DonorDonation)
admin.site.register(Funder)

admin.site.register(Sponsorship)
admin.site.register(Sponsor)
admin.site.register(SponsorSponsorship)
# Register your models here.
