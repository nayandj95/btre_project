from datetime import datetime
from django.db import models
from realtors.models import Realtor

# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    pthoto_main = models.ImageField(upload_to = 'photo/%y/%m/%d/')
    pthoto_1 = models.ImageField(upload_to = 'photo/%Y/%m/%d/', blank=True)
    pthoto_2 = models.ImageField(upload_to = 'photo/%Y/%m/%d/', blank=True)
    pthoto_3 = models.ImageField(upload_to = 'photo/%Y/%m/%d/', blank=True)
    pthoto_4 = models.ImageField(upload_to = 'photo/%Y/%m/%d/', blank=True)
    pthoto_5 = models.ImageField(upload_to = 'photo/%Y/%m/%d/', blank=True)
    pthoto_6 = models.ImageField(upload_to = 'photo/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    def __str__(self):
        return self.title
