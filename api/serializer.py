from rest_framework import serializers

from .models import Contacts

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Contacts
        fields = '__all__'



class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ["id","fname","lname"]