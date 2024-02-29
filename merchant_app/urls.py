from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from merchant_app import views


urlpatterns = [
    path('merchants/', views.MerchantList.as_view()),
    path('merchant/<int:pk>', views.MerchantDetail.as_view()),
]
