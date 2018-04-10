from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from .models import User_details, Payment_details, Meter_details
from .serializers import UserSerializer, PaymentSerializer
from paytm.payments import PaytmPaymentPage
from paytm import Checksum
from django.http import HttpResponse
from paytm.payments import VerifyPaytmResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

# def signup(request):
    


def payment(request):
    order_id = Checksum.__id_generator__()
    bill_amount = "100"
    cust_id = "payment_maker@email.com"
    data_dict = {
                'ORDER_ID':order_id,
                'TXN_AMOUNT': bill_amount,
                'CUST_ID': cust_id
            }
    return PaytmPaymentPage(data_dict)
    

@csrf_exempt
def response(request):
    resp = VerifyPaytmResponse(request)
    if resp['verified']:
        # save success details to db
        print(resp['paytm']['ORDERID'])  #SAVE THIS ORDER ID TO DB FOR TRANSACTION HISTORY
        return JsonResponse(resp['paytm'])
    else:
        return HttpResponse("Verification Failed")
    return HttpResponse(status=200)

