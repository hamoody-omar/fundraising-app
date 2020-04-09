from django.contrib import admin
from .models import Donation, Donor, DonorDonation, Funder


admin.site.register(Donation)
admin.site.register(Donor)
admin.site.register(DonorDonation)
admin.site.register(Funder)
# Register your models here.
