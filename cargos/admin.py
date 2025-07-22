from django.contrib import admin

from cargos.models import CargoTransport, CargoDimension


class CargoTransportAdmin(admin.ModelAdmin):
    list_filter = [
        "collection_date",
        "collection_address",
        "delivery_address",
        "transport_duration"
    ]
    list_per_page = 25
    ordering = ["-collection_date"]


class CargoDimensionAdmin(admin.ModelAdmin):
    list_filter = [
                    "cargo",
                    "length",
                    "width",
                    "height",
                    "weight",
                    ]
    ordering = ["cargo"]
    list_per_page = 25


admin.site.register(CargoTransport, CargoTransportAdmin)
admin.site.register(CargoDimension, CargoDimensionAdmin)
