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
    payment_amount = serializers.IntegerField()

    class Meta:
        fields = ('payment_amount',)