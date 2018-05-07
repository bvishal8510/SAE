from django.contrib import admin
from meter.models import Payment_details, Customer
# , Payment_details, Meter_details
# Register your models here.
admin.site.register(Customer)
admin.site.register(Payment_details)
# admin.site.register(Meter_details)