from rest_framework import serializers
from meter.models import User_details
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User_details
        fields = ('name', 'email',)


class PaymentSerializer(serializers.Serializer):
    customer_id = serializers.CharField(max_length=100)
    payment_amount = serializers.IntegerField()

    class Meta:
        fields = ('customer_id', 'payment_amount',)