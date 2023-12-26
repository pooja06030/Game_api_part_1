from django.contrib import admin
from django.contrib import admin
from Game_api.models import  Developer
from  Game_api.models import GameMaker 
from  Game_api.models import GameMaker 
from  Game_api.models import device_frant
# from jio_app.models import store_frant
# Register your models here.

class  GameMakerAdmin(admin.ModelAdmin):
    list_display=['game_name', 'game_type', 'game_price', 'is_active', 'include_ads','developer']

admin.site.register(GameMaker , GameMakerAdmin)

class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'address', 'create_at', 'update_at']

admin.site.register(Developer , DeveloperAdmin)


class device_frant_Admin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(device_frant , device_frant_Admin)

# class store_frant_Admin(admin.ModelAdmin):
#     list_display = ['Game', 'device']

# admin.site.register(store_frant , store_frant_Admin)

    
    




# Register your models here.
