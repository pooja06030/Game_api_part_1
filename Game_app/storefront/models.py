from django.db import models
from django.db import models
from Game_api.models import GameMaker, device_frant
# Create your models here.
class store_frant(models.Model):
   Game= models.ForeignKey(GameMaker,on_delete=models.CASCADE, default=None, blank=True, related_name = 'store_game')
   device = models.ForeignKey(device_frant, on_delete=models.CASCADE, default=None, blank=True, related_name = 'store_divice')

#    def __str__(self):
#     return f'{self.Game} {self.device}'



class category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    category_description = models.TextField(max_length=254)
    category_image = models.ImageField(upload_to='category_images', max_length=200)  
    category_icon_upload = models.FileField(upload_to='category_icons', max_length=500)  
    category_icon_url = models.URLField(max_length=200)  
    active = models.BooleanField(default=True)  
    category_subtitle = models.CharField(max_length=100)
    notes = models.CharField(max_length=254)
    
    def __str__(self):
        return self.category_name  









# Create your models here.
