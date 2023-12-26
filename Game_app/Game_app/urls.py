from django.contrib import admin
from django.urls import path,include
from Game_api import views
from rest_framework.routers import DefaultRouter
from storefront.views import test



router = DefaultRouter()


router.register('GameMakerapi', views.GameMakerSerializerViewSet, basename='GameMaker')
router.register('Developerapi', views.DeveloperSerializerViewSet, basename='Developer')
router.register('Game_Developer_api', views.Developer_games_SerializerViewSet, basename='Game_Developer')



#  path('approved/<int:pk>', views.approved, name='approved'),  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('storefront/',include('storefront.urls'))

]
