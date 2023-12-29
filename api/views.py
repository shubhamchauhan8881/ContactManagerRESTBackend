from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializer
# Create your views here.
class showContacts(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        if pk != None:
            c =  models.Contacts.getContact(pk)
            if c == "NE": return Response({"message":"error", "error_message": "contact does not exist!!"})
            s = serializer.ContactSerializer(c, many=False)

        else:  
            c =  models.Contacts.getContact()
            s = serializer.ContactSerializer(c, many=True)
        return Response({"message":"ok","data":s.data})
        
    


class AddNewContact(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serial = serializer.ContactSerializer(data = data)
        if serial.is_valid():
            serial.save()
            return Response({"message":"ok", "data": serial.data})
        else:
            return Response({"message":"error", "error_message": serial.errors})

    # to save edited contacts
    def patch(self, request, pk=None, *args, **kwargs):
        data = request.data
        c = models.Contacts.getContact(int(data['id']))
        s = serializer.ContactSerializer(c, data=data, partial=True)
        if s.is_valid():
            s.save()
            return Response({"message":"ok","data":s.data})
        else:
            return Response({"message":"error", "error_message": s.data})


class DeleteContact(APIView):
    def post(self, request,pk=None, *args, **kwargs):
        if pk is not None:
            try:
                objects = models.Contacts.getContact(pk)
                objects.delete()
                return Response({"message":"ok"})
            except:
                return Response({"message":"error", "error_message":"contact with gievn id does not exists!"})
        else:
            return Response({"message":"error", "error_message":"invalid request!!"})


class MarkFav(APIView):
    def post(self, request,pk,*args, **kwargs):
        obj = models.Contacts.getContact(pk)
        obj.is_fav = not obj.is_fav
        obj.save()
        return Response({"message":"ok"})


class Search(APIView):
    def post(self, request,search_string,*args, **kwargs):
        results = models.Contacts.getLike(search_string=search_string)
        if results:
            s = serializer.SearchSerializer(results, many=True)
            return Response({"message":"ok","data":s.data})
        else:
            return Response({"message":"error","error_message":"no matching results"})