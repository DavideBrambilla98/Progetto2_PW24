from django.contrib import admin
# Register your models here.
from .models import PatologiaTable

class TableAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    list_filter = ['nome','codice']
    search_fields = ['nome','codice']

    class Meta:
        model = PatologiaTable

admin.site.register(PatologiaTable, TableAdmin)