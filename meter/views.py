from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from meter.models import User_details, Payment_details
from meter.serializers import UserSerializer, PaymentSerializer
from paytm.payments import PaytmPaymentPage
from paytm import Checksum
from django.http import HttpResponse
from paytm.payments import VerifyPaytmResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
import json


class LoginViewSet(viewsets.ModelViewSet):
    
    queryset = User_details.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post',]

    def perform_create(self, serializer):
        serializer.save()
        return Response(serializer.data,
        #  "meter/index.html", 
         status=status.HTTP_201_CREATED)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment_details.objects.all()
    serializer_class = PaymentSerializer
    http_method_names = ['post',]

    def perform_create(self, serializer):
        order_id = Checksum.__id_generator__()
        bill_amount = serializer["payment_amount"]
        cust_id = serializer["customer_id"]
        data_dict = {
                'ORDER_ID':order_id,
                'TXN_AMOUNT': bill_amount,
                'CUST_ID': cust_id
                }
        print(PaytmPaymentPage(data_dict))
        return PaytmPaymentPage(data_dict)
        

class ResponseViewSet(viewsets.ViewSet):
    queryset = Payment_details.objects.all()
    serializer_class = PaymentSerializer
    http_method_names = ['get',]
    
    def get(self, request):
        resp = VerifyPaytmResponse(request)
        if resp['verified']:
            print(resp['paytm']['ORDERID'])  
            return JsonResponse(resp['paytm'])
        else:
            return HttpResponse("Verification Failed")
    
# def response(request):
#     resp = VerifyPaytmResponse(request)
#     if resp['verified']:
#         # save success details to db
#         print(resp['paytm']['ORDERID'])  #SAVE THIS ORDER ID TO DB FOR TRANSACTION HISTORY
#         return JsonResponse(resp['paytm'])
#     else:
#         return HttpResponse("Verification Failed")
#     return HttpResponse(status=200)
# def payment(request):
#     serializer = PaymentSerializer(data=request, context={'request': request})
#     print(request)
#     if serializer.is_valid():
#         order_id = Checksum.__id_generator__()
#         bill_amount = "100"
#         cust_id = "payment_maker@email.com"
#         data_dict = {
#                 'ORDER_ID':order_id,
#                 'TXN_AMOUNT': bill_amount,
#                 'CUST_ID': cust_id
#                 }
#         print(7)
#         return PaytmPaymentPage(data_dict)
#         # return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# # @api_view(['GET'])
