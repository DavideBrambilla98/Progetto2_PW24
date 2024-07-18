from django.contrib import admin
# Register your models here.
from .models import PatologiaTable

class TableAdmin(admin.ModelAdmin):
    list_display = ['__str__','codice', 'nome','criticita','cronica','mortale']
    list_filter = ['nome','codice']
    search_fields = ['nome','codice']
    prepopulated_fields = {'slug':('titolo',)}

    class Meta:
        model = PatologiaTable

admin.site.register(PatologiaTable, TableAdmin)