from django.contrib import admin
from . import models

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'telephone')
    list_filter = ('vehicle',)
    search_fields = ('id','name')

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('owner', 'board')
    list_filter = ('owner',)
    search_fields = ('id','owner','board')

class RotaryAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'input', 'output', 'paid', 'total_hour')

class MonthlyAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'input', 'output', 'paid', 'total_month')

admin.site.register(models.Vehicle, VehicleAdmin)
admin.site.register(models.People, PeopleAdmin)
admin.site.register(models.Brand)
admin.site.register(models.Parameter)
admin.site.register(models.Rotary, RotaryAdmin)
admin.site.register(models.Monthly, MonthlyAdmin)
