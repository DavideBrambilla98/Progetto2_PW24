from django.contrib import admin

# Register your models here.

from .models import PatologiaTable, RicoveroTable, OspedaleTable, PersoneTable, PatologiaRicoveroTable



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

class PersoneTableAdmin(admin.ModelAdmin):
    list_display = ['codFiscale']
    list_filter = ['codFiscale']
    search_fields = ['codFiscale']

    class Meta:
        model = PersoneTable

class PatologiaRicoveroTableAdmin(admin.ModelAdmin):
    list_display = ['codOspedale','codRicovero','codPatologia']
    list_filter = ['codOspedale','codRicovero','codPatologia']
    search_fields = ['codOspedale','codRicovero','codPatologia']

    class Meta:
        model = PatologiaRicoveroTable

admin.site.register(PatologiaTable, PatologiaTableAdmin)
admin.site.register(RicoveroTable, RicoveroTableAdmin)
admin.site.register(OspedaleTable, OspedaleTableAdmin)
admin.site.register(PersoneTable, PersoneTableAdmin)
admin.site.register(PatologiaRicoveroTable, PatologiaRicoveroTableAdmin)
