from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from .models import GameMaker
from .models import  Developer
from .serializers import GameMakerSerializer
from .serializers import  DeveloperSerializer
from rest_framework import status
from rest_framework import viewsets
# from django.core.serializers import Serializer


# Create your views here.


class GameMakerSerializerViewSet(viewsets.ViewSet):
 def list(self, request):
  stu = GameMaker.objects.all()
  serializer = GameMakerSerializer(stu, many=True)
  return Response(serializer.data)
 

class DeveloperSerializerViewSet(viewsets.ViewSet):
 def list(self, request):
  stu = Developer.objects.all()
  serializer = DeveloperSerializer(stu, many=True)
  return Response(serializer.data) 
 

#values to ho gya ab mujhe count lgana he jese id 3 wale ne 2 game bnaye to id=3 hit kru postman se to 2 count aana chahiye id=1 wale ne ek game bnaya to count 1 aana chahiye
#means game ki id ko count krna 
#loop ke under count nhi lgana he kyki loop me count replace ho jayega mtlab count ka alg se function bnaya us count function ko men function me loop ke uper call kro us function ki key bnakr ek list me appned kr do
class Developer_games_SerializerViewSet(viewsets.ViewSet):
    def list(self,request):
      dev_id=request.data.get('id')
      if dev_id:
        game_makers=GameMaker.objects.filter(developer_id=dev_id).values('id','developer_id','game_name','game_price','game_type')
        print('###########',game_makers)
      else: 
        game_makers=GameMaker.objects.all() #query object ke data ko dict me covert krna pega kyuki ye json dict hi leta he 

      data=[]
      d={}
      d['count']=count_data(game_makers)
      data.append(d)
      for game_maker in game_makers:
          game_data={}
          developer_id=game_maker.get('developer_id')
          developer_fun=get_developer_data(developer_id)
          game_data['include_ads']=game_maker.get('include_ads')
          game_data['game_name']=game_maker.get('game_name')
          game_data['game_price']=game_maker.get('game_price')
          game_data['game_type']=game_maker.get('game_type') 
          game_data['developer_func'] =developer_fun
          data.append(game_data)
      return Response(data)
  
  
 
def get_developer_data(developer_id): 
    data= Developer.objects.filter(id=developer_id).first()
    print(data)
    developer_data={}
    developer_data['name']=data.name
    developer_data['email']=data.email
    developer_data['address']=data.email
    developer_data['address']=data.address
    developer_data['privacy_policy']=data.privacy_policy
    developer_data['create_at']=data.create_at
    developer_data['updated_at']=data.update_at
    return developer_data

def count_data(game_makers):
    count=0
    for i in game_makers:
      if i['id']:
        count += 1
    return count  


     

 
   



  
  
 
