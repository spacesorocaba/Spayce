from django.apps import apps
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from spayce.models import Spacer

app = apps.get_app_config('spayce')


class OrderAdmin(admin.ModelAdmin):
    ordering = ('-timestamp',)
    list_display = ('customer', 'item', 'quantity',
                    'receipt_value', 'paid')
    list_filter = ('customer', 'paid')

    def get_owner(self, obj):
        return obj.industrial_element.owner
    get_owner.short_description = 'Owner'
    get_owner.admin_order_field = 'industrial_element__owner'


AdminDict = {'order': OrderAdmin,}


for model_name, model in app.models.items():
    if model_name in AdminDict:
        admin.site.register(model, AdminDict[model_name])
    else:
        admin.site.register(model)

admin.site.unregister(Spacer)
admin.site.register(Spacer, UserAdmin)
