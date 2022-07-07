from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(ClientInformations)
admin.site.register(ArtistInformation)
admin.site.register(Service)
admin.site.register(Voucher)
admin.site.register(Payment)