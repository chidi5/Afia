from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *


# Register your models here.

class ViewAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Product, ViewAdmin)
admin.site.register(Category, ViewAdmin)
admin.site.register(Device, ViewAdmin)
admin.site.register(Type, ViewAdmin)
admin.site.register(Model, ViewAdmin)
admin.site.register(Memory, ViewAdmin)
admin.site.register(Storage, ViewAdmin)
admin.site.register(Color, ViewAdmin)
admin.site.register(Images, ViewAdmin)
admin.site.register(Comment, ViewAdmin)
