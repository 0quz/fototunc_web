from django.contrib import admin
from .models import Tracking
# Register your models here.
# tracking sistemini admin paneline ekledik
class TrackingAdmin(admin.ModelAdmin):
    # admin sayfası üzerinde gösterme
    list_display = ['name', 'surname', 'tracking_number', 'publishing_date', 'slug']
    # listeyi yönlendirilebilir yapma
    list_display_links = ['name', 'surname', 'tracking_number', 'publishing_date']
    # tarihe göre filtre oluşturma
    list_filter = ['publishing_date']
    # arama çubuğu ekleme
    search_fields = ['name', 'surname', 'tracking_number']
    # listeye güncelleme yapma
    # list_editable = ['name', 'surname']
    # editable=False admin panelinden kaldır slugı
    # prepopulated_fields = {'slug': ('tracking_number',)}

    class Meta:
        model = Tracking

admin.site.register(Tracking, TrackingAdmin)