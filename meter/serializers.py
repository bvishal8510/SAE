from rest_framework import serializers
from meter.models import Payment_details
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email','password')

class ForgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username')

class PaymentSerializer(serializers.Serializer):
    customer_id = serializers.CharField(max_length=100)
    payment_amount = serializers.IntegerField()

    class Meta:
        fields = ('customer_id', 'payment_amount',)