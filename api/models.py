from django.db import models

# Create your models here.
class Contacts(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    is_fav= models.BooleanField(default=False)
    
    def __str__(self):
        return self.fname
    
    @staticmethod
    def getContact(pk=None):
        if pk is None:
            return Contacts.objects.all()
        else:
            try:
                return Contacts.objects.get(id=pk)
            except Contacts.DoesNotExist as e:
                return 'NE' #not exists

    @staticmethod
    def getByName(name):
        return Contacts.objects.filter(name=name)
    
    @staticmethod
    def getLike(search_string):
        if search_string.isdigit():
            return Contacts.objects.filter(phone__contains=search_string)
        return Contacts.objects.filter(fname__contains=search_string)

