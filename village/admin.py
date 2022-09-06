from django.contrib import admin
from .models import FundRequest, Village
# Register your models here.


class VillageAdmin(admin.ModelAdmin):
    # search_fields = ['email', 'first_name', 'last_name']
    pass
    

class FundRequestAdmin(admin.ModelAdmin):
    search_fields = ['email', 'first_name', 'last_name']
    list_display = ['user','request_title','How_much_do_you_need','request_confirmed',]
    

admin.site.register(Village, VillageAdmin)
admin.site.register(FundRequest, FundRequestAdmin)



