from django.contrib import admin
from ..calculate.models import PriceData

@admin.register(PriceData)
class PriceDataAdmin(admin.ModelAdmin):
    list_display = ('tipe_kertas', 'gramatur_kertas', 'ukuran_kertas', 'harga')

