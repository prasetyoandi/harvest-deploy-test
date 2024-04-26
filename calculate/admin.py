from django.contrib import admin
from .models import PriceData, ProductionPrice, LaminateCost, FinishingCost

@admin.register(PriceData)
class PriceDataAdmin(admin.ModelAdmin):
    list_display = ('plano_besar', 'plano_kecil', 'tipe_kertas', 'ukuran_kertas', 'harga')

@admin.register(ProductionPrice)
class ProductionPriceAdmin(admin.ModelAdmin):
    list_display = ('production_cost', 'set_warna', 'harga_produksi')

@admin.register(LaminateCost)
class LaminateCostAdmin(admin.ModelAdmin):
    list_display = ('length', 'width', 'get_laminate_type_display', 'harga_laminasi')

    def get_laminate_type_display(self, obj):
        return obj.get_laminate_type_display()
    get_laminate_type_display.short_description = 'Laminate Type'

@admin.register(FinishingCost)
class FinishingCostAdmin(admin.ModelAdmin):
    list_display = ('tipe_finishing', 'harga_finishing')