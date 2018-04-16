from django.db import models

class User_details(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=70,blank=False)
    Token = models.CharField(max_length=200,blank=False)

class Payment_details(models.Model):
    customer_id = models.CharField(max_length=100, blank=False)
    payment_amount = models.IntegerField(blank=False)
    order_id = models.CharField(max_length=100, blank=False)
    

# class Meter_details(models.Model):
#     meter_no = models.IntegerField(blank=False)
#     elec_remain = models.IntegerField(blank=False, default = 0)
