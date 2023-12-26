from django.contrib import admin
from django.contrib import admin
from storefront.models import store_frant
from storefront.models import category
# Register your models here.

class store_frantAdmin(admin.ModelAdmin):
    list_display = ['Game', 'device']

admin.site.register(store_frant , store_frantAdmin)

class category_Admin(admin.ModelAdmin):
    list_display = ['id', 'category_name','category_description','category_image','category_icon_upload','category_icon_url','active','category_subtitle','notes']

admin.site.register(category , category_Admin)


# Register your models here.
