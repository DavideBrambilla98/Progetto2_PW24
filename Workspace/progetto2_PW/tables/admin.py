from django.contrib import admin
from .models import PatologiaTable, RicoveroTable, OspedaleTable


class PatologiaTableAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    list_filter = ['nome','codice']
    search_fields = ['nome','codice']

    class Meta:
        model = PatologiaTable

class RicoveroTableAdmin(admin.ModelAdmin):
    list_display = ['codiceRicovero']
    list_filter = ['codiceRicovero']
    search_fields = ['codiceRicovero']

    class Meta:
        model = RicoveroTable

class OspedaleTableAdmin(admin.ModelAdmin):
    list_display = ['denominazioneStruttura']
    list_filter = ['denominazioneStruttura']
    search_fields = ['denominazioneStruttura']

    class Meta:
        model = OspedaleTable

admin.site.register(PatologiaTable, PatologiaTableAdmin)
admin.site.register(RicoveroTable, RicoveroTableAdmin)
admin.site.register(OspedaleTable, OspedaleTableAdmin)
