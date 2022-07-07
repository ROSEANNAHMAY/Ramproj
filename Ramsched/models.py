from django.db import models
import uuid

# Create your models here.
class ClientInformations(models.Model):
    GENDER_TYPES = (
            ('M', 'Male'),
            ('F', 'Female'),
            )
    last = models.CharField(max_length=24)
    first = models.CharField(max_length=24)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=11,)
    gender = models.TextField(max_length=1,choices=GENDER_TYPES)
    age = models.PositiveIntegerField()

    def __str__(self):
         return '%s-%s' % (self.first, self.last)
 
class ArtistInformation(models.Model):
    artistname = models.CharField(max_length=24)

    def __str__(self):
        return self.artistname

class Service(models.Model):
    SERVICE_TYPES = (
        ('Tattoo', 'Tattoo'),
        ('Henna', 'Henna'),
        ('Piercing', 'Piercing'),
        )
    service_artist = models.ForeignKey(ArtistInformation, on_delete=models.CASCADE)
    service_client = models.ForeignKey(ClientInformations, on_delete=models.CASCADE)
    service_date = models.DateField()
    service_type = models.CharField(max_length=24,choices=SERVICE_TYPES)

    def __str__(self):
        return '%s-%s' % (self.service_artist, self.service_client)

class Voucher(models.Model):
    VOUCHER_TYPES = (
        ('30', '30 percent'),
        ('40', '40 percent'),
        ('50', '50 percent'),
        )
    voucher_name = models.CharField(max_length=120,
            unique=True,
            primary_key=True,
            default=uuid.uuid4)
    voucher_type = models.TextField(choices=VOUCHER_TYPES)
    voucher_date = models.DateField()
    def __str__(self):
        return self.voucher_name

class Payment(models.Model):
    PAYMENT_METHOD = (
        ('G', 'Gcash'),
        ('C', 'Cash'),
        ('P', 'Paymaya'),
        )
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    payment_voucher  = models.ForeignKey(Voucher, on_delete=models.CASCADE,null=True,blank=True)
    payment_method = models.CharField(max_length=1,choices=PAYMENT_METHOD)

    def __str__(self):
        return '%s-%s' % (self.payment_method, self.id)
