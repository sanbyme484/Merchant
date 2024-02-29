from rest_framework import serializers

from merchant_app.models import Merchant


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = ['name', 'description', 'description_html', 'email', 'phone_number']