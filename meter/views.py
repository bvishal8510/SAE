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
from rest_framework.decorators import api_view



# def signup(request):
    

# @api_view(['POST'])
def payment(request):
    # serializer = PaymentSerializer(data=request.data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    order_id = Checksum.__id_generator__()
    bill_amount = "100"
    cust_id = "payment_maker@email.com"
    data_dict = {
                'ORDER_ID':order_id,
                'TXN_AMOUNT': bill_amount,
                'CUST_ID': cust_id
            }
    print(5)
    print(PaytmPaymentPage(data_dict))
    print(7)
    return PaytmPaymentPage(data_dict)
    print(6)
    

@csrf_exempt
@api_view(['GET'])
def response(request):
    resp = VerifyPaytmResponse(request)
    if resp['verified']:
        # save success details to db
        print(resp['paytm']['ORDERID'])  #SAVE THIS ORDER ID TO DB FOR TRANSACTION HISTORY
        return JsonResponse(resp['paytm'])
    else:
        return HttpResponse("Verification Failed")
    return HttpResponse(status=200)

