from django.contrib import admin

from merchant_app.models import Merchant


@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    pass
