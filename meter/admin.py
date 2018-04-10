from django.contrib import admin
from .models import User_details, Payment_details, Meter_details
# Register your models here.
admin.site.register(User_details)
admin.site.register(Payment_details)
admin.site.register(Meter_details)