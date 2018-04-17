from django.conf.urls import url, include
# from meter.views import payment, response
from meter import views
from rest_framework.routers import DefaultRouter
# from rest_framework.schemas import get_schema_view



router = DefaultRouter()
router.register(r'login', views.LoginViewSet)
router.register(r'payment', views.PaymentViewSet)
# router.register(r'response', views.ResponseViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^schema/$', schema_view),
]