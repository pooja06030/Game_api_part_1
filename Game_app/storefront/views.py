from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from django.http.response import JsonResponse
from Game_api.models import GameMaker
from Game_api.models import  Developer
from Game_api.models import device_frant
from rest_framework import status
from rest_framework import viewsets
from storefront.models import store_frant
import json
# Create your views here.



      
def test(request): 
    if request.method == 'GET':
        store_id = request.GET.get('id')
        print('@@@@@@@',store_id)
        if store_id:
            store_data = store_frant.objects.filter(device_id=store_id)
        else:
            store_data = store_frant.objects.all()

        dev_data = []
        for data in store_data:
            data_store_frant = {}
            device_id = data.device_id
            device_fun=device_data(device_id)
            data_store_frant['device_detail']=device_fun
            game_id = data.Game_id
            game_fun=game_data(game_id)
            data_store_frant['game_detail']=game_fun
            dev_data.append(data_store_frant)
        
        return JsonResponse(dev_data, safe=False)
    

def device_data(device_id): 
    data= device_frant.objects.filter(id=device_id)
    for val in data:
      device={}
      device['device_id']=val.id
      device['device_name']=val.name
      return device
    
def game_data(game_id):
    data=GameMaker.objects.filter(id=game_id).values('id','developer_id','game_name','game_price','game_type')
    for val in data:
        game={}
        developer_id=val.get('developer_id')
        developer_fun=developer_data(developer_id)
        game['game_id']=val.get('id')
        game['game_name']=val.get('game_name')
        game['game_price']=val.get('game_price')
        game['game_type']=val.get('game_type')
        game['developer_detail'] =developer_fun
        return game
    

def developer_data(developer_id): 
   data= Developer.objects.filter(id=developer_id)
   for val in data:
      developer={} 
      developer['name']=val.name
      developer['email']=val.email
      developer['address']=val.email
      developer['address']=val.address
      developer['privacy_policy']=val.privacy_policy
      developer['create_at']=val.create_at
      developer['updated_at']=val.update_at
      return developer

       
      

        
    
        
    

    
# Create your views here.
