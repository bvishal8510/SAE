from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User
from payments import PurchasedItem
from payments.models import BasePayment
from django.db import models


class Payment(BasePayment):
    
    user = models.ForeignKey(User, default=None)
    variant=models.CharField(max_length=100, blank=False),  # this is the variant from PAYMENT_VARIANTS
    # description=models.CharField(max_length=500, blank=True),
    # total=models.IntegerField(blank=False),

    def get_failure_url(self):
        return 'http://example.com/failure/'

    def get_success_url(self):
        return 'http://example.com/success/'

    def get_purchased_items(self):
        # you'll probably want to retrieve these from an associated order
        yield PurchasedItem(name='The Hound of the Baskervilles', sku='BSKV',
                            quantity=9, price=Decimal(10), currency='USD')
