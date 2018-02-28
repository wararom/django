from django.contrib import admin
from rent.models import Rent,Car,Person


class RentAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Rent._meta.fields]
    list_editable=('stop','fee')
admin.site.register(Rent,RentAdmin)

class CarAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Car._meta.fields]
admin.site.register(Car,CarAdmin)

class PersonAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Person._meta.fields]
admin.site.register(Person,PersonAdmin)
