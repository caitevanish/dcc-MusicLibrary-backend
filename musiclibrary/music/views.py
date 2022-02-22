from django.http import Http404
from django.shortcuts import render

#used within endpoint class-based view methods:
from .models import Song 
from .serializers import SongSerializer 

#parent class for our class-based views. Takes care of method routing
from rest_framework.views import APIView 

#function call that converts our data into a JSON string literal, sends to the client 
from rest_framework.response import Response 

#Status is an enum, a collection of values, that specify status code we would like to send back in the response.
from rest_framework import status


# Create your views here.
class SongList(APIView):

  def get(self, request): #request parameter is an OBJECT that contains info about client's request
    song = Song.objects.all() 
    serializer = SongSerializer(song, many = True) #many = object with many rows
    return Response(serializer.data)

  def post(self,request):
    serializer = SongSerializer(data=request.data)#take the data from body of request, pass it into new instantiation of the serializer
    if serializer.is_valid(): #confirm the request's data contains all req fields present on model definition
      serializer.save() #if true, then save will convert request's JSON data into a new model instance, save it to table in db
      return Response(serializer.data, status=status.HTTP_201_CREATED) #return serializer.data in response object, specify 201 code
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  #before testing API in postman set up app's URLs!

class SongDetail(APIView):
#get by id
  def get_song(self, pk):
    try:
      return Song.objects.get(pk=pk)
    except Song.DoesNotExist:
      raise Http404

  def get(self, request, pk):
    song = self.get_song(pk)
    serializer = SongSerializer(song)
    return Response(serializer.data)

 #update
  def put(self,request, id):
    song = self.get_song(id)
    serializer = SongSerializer(song, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #delete
  def delete(self, request, id):
    song = self.get_song(id)
    song.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    
  
class SongLike(APIView):
  def get_song(self, id):
    try:
      return Song.objects.get(pk=id)
    except Song.DoesNotExist:
      raise Http404

  def like(self, request, id):
    song = self.get_song(id)                                                #getting song
    serializer = SongSerializer(song, data=request.data)                    #
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)
