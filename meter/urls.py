from django.conf.urls import url, include
from meter.views import payment, response
from meter import views

urlpatterns = [
    url(r'^payment/', views.payment, name='payment'),
    url(r'^response/', views.response, name='response'),
]