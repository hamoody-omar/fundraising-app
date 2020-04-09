from django.db import models
from django.utils.timezone import now
from datetime import timedelta, datetime

class Donation(models.Model):
    name = models.CharField(max_length=200, default='')
    goal = models.CharField(max_length=2000, default='')
    amount = models.DecimalField(decimal_places=2, max_digits=100, default=0)
    created_at = models.DateTimeField(default=now)
    starts_at = models.DateTimeField(default=now)
    ends_at = models.DateTimeField(default=(datetime.now() + timedelta(weeks=4)))

    def __str__(self):
        return self.name

class Donor(models.Model):
    full_name = models.CharField(max_length=200, default='Anonymous')
    amount = models.DecimalField(decimal_places=2, max_digits=100, default=0)
    email_address = models.CharField(max_length=200, default='')
    phone_number = models.CharField(max_length=20, default='')
    created_at = models.DateTimeField(default=now)

class DonorDonation(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE, verbose_name="the related donation", db_index=True)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, verbose_name="the related donor", db_index=True)

class Sponsorship(models.Model):
    name = models.CharField(max_length=200, default='')
    goal = models.CharField(max_length=2000, default='')
    amount = models.DecimalField(decimal_places=2, max_digits=100, default=0)
    created_at = models.DateTimeField(default=now)

class Sponsor(models.Model):
    company_name = models.CharField(max_length=200, default='')
    offer_description = models.CharField(max_length=10000, default='')
    offer = models.DecimalField(decimal_places=2, max_digits=100, default=0)
    website_url = models.CharField(max_length=200, default='')
    business_email_address = models.CharField(max_length=200, default='')
    business_phone_number = models.CharField(max_length=20, default='')
    is_offer_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.company_name

class SponsorSponsorship(models.Model):
    sponsorship = models.ForeignKey(Sponsorship, on_delete=models.CASCADE, verbose_name="the related sponsorship", db_index=True)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, verbose_name="the related sponsor", db_index=True)

class Funder(models.Model):
    organization_name = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=10000, default='')
    amount = models.DecimalField(decimal_places=2, max_digits=100, default=0)
    website_url = models.CharField(max_length=200, default='')
    organization_email_address = models.CharField(max_length=200, default='')
    organization_phone_number = models.CharField(max_length=20, default='')
    created_at = models.DateTimeField(default=now)
