from django.contrib import admin

# Register your models here.

from .models import CIMC_Production, CIMC_Part

class CIMC_ProductionAdmin(admin.ModelAdmin):
    fields = ['item',
              'jobNumber',
              'machNo',
              'partWeight',
              'cavityID',
              'headID',
              'activeCavities',
              'dateCreated',
              'inProduction']

admin.site.register(CIMC_Part)
admin.site.register(CIMC_Production,CIMC_ProductionAdmin)