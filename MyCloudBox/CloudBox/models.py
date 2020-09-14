from django.db import models
#from storages.backends.azure_storage import AzureStorage

# Create your models here.
class user(models.Model):
    
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    mobile = models.CharField(max_length = 10)
    email = models.EmailField()
    dob = models.DateField()
    gender = models.CharField(max_length = 20)
    company = models.CharField(max_length = 20)
    address = models.CharField(max_length = 20)
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)

'''
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
'''