from django.db import models
from django.utils.timezone import now
from realtors.models import Realtor


class Photo(models.Model):
    listing = models.ForeignKey('Listing', on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')

    def __str__(self):
        return self.listing.title


class Listing(models.Model):
    class SaleType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'

    class HomeType(models.TextChoices):
        HOUSE = 'HOUSE'
        CONDO = ' CONDO'
        TOWNHOUSE = 'TOWNHOUSE'

    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    sale_type = models.CharField(max_length=30, choices=SaleType.choices, default=SaleType.FOR_SALE)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    home_type = models.CharField(max_length=30, choices=HomeType.choices, default=HomeType.HOUSE)
    sqft = models.IntegerField()
    open_house = models.BooleanField(default=False)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)

    def format_data(self):
        return {'id': self.pk, 'title': self.title, 'slug': self.slug}

    def __str__(self):
        return self.title
