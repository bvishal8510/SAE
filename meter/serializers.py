from rest_framework import serializers
from meter.models import User_details, Payment_details
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User_details
        fields = ('name', 'email', 'meter_no',)


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment_details
        fields = ('customer_id', 'payment_amount',)