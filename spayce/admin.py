from django.apps import apps
from django.contrib import admin

# Register your models here.

app = apps.get_app_config('spayce')

AdminDict = {}


for model_name, model in app.models.items():
    if model_name in AdminDict:
        admin.site.register(model, AdminDict[model_name])
    else:
        admin.site.register(model)
