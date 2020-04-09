from django.contrib import admin
from .models import Donation, Donor, DonorDonation

admin.site.register(Donation)
admin.site.register(Donor)
admin.site.register(DonorDonation)
# Register your models here.
