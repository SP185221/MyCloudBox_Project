from .models import user
from django.http import HttpResponse
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

# Create your views here.


def registration(request):
    f = request.POST['first-name']
    l = request.POST['last-name']
    m = request.POST['mobile']
    e = request.POST['email']    
    d = request.POST['dob']    
    g = request.POST['gender']    
    c = request.POST['company']  
    a = request.POST['address']    
    u = request.POST['username']    
    p1 = request.POST['password1'] 
    p2 = request.POST['password2']      

    emps = user.objects.filter( username = u)

    if len(emps) > 0:
        return render(request, "registration.html", { 'availability' : 'Username Not Available' })
    else:
        if p1 == p2:
            upload = user(firstname = f, lastname = l, mobile = m, email = e, dob = d, gender = g, company = c, address =  a, username = u, password =  p1 )
            upload.save()
            emps = user.objects.filter( username = u)
            Container_create(u)
            return render(request , 'display.html', {'emps' : emps, 'welcome' : 'Congratulations Account Created' },)
        else:
            return render(request, "registration.html", { 'password_validation' : 'Password Not match' })
    #return HttpResponse("Thanks !!! User Created")


def create(request):
    return render(request , 'registration.html')
def login(request):
    return render(request, "login.html")

def display(request):
    
    us = request.POST['user']
    ps = request.POST['pass']
    emps = user.objects.filter( username = us)
    
    if len(emps) > 0 :
        for emp in emps:
            if emp.password == ps:
                file_list = Container_list(us)
                return render(request, 'simple_upload.html',{'user_name' : us,'list_of_files' : file_list  })
                #return render(request , 'display.html', {'emps' : emps },)
            else:
                return render(request, "login.html", { 'invalid' : 'Invalid Password' })
    else:
        return render(request, "login.html", { 'invalid' : 'Invalid User' })
    
def delete_account(request):
    un = request.POST['uname']
    emps = user.objects.filter( username = un)
    emps.delete()
    Container_delete(un)
    return render(request, "login.html")

def change_password(request):
    un = request.POST['uname']
    return render(request, "passwordchange.html",  { 'username' : un })


def change_password_page(request):
    un = request.POST['uname']
    ps1 = request.POST['pass1']
    ps2 = request.POST['pass2']
    if ps1 == ps2:
        a = user.objects.get( username = un)
        a.password = ps1
        a.save()
        return render(request, "passwordchange.html",  { 'confimation' : 'Password Changed successfully', 'username' : un  })
    else:
        return render(request, "passwordchange.html",  { 'confimation' : 'Password not macthed', 'username' : un  })

#Azure Codes for views Statred here 

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        cn = request.POST['cname']
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        return_value = upload_blob(filename,cn)
        file_list = Container_list(cn) 
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', { 'user_name' : cn, 'uploaded_file_url': return_value , 'list_of_files' : file_list } )
    else:
        return render(request, 'simple_upload.html')
    
def Container_create(c_name):
    try:
        connect_str = "DefaultEndpointsProtocol=https;AccountName=globalmicrotel;AccountKey=wsLwVILrwM+6RKwnkqQLORiUeLozc0odFqeNZyhRexkNUWxIddDnbVuR3jN7wz2nW+/1ry6mDx+hL3WN5t35xw==;EndpointSuffix=core.windows.net"
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        container_name = c_name
        #print("Container Creation started ....\n")
        container_client = blob_service_client.create_container(container_name)
        #print("Value of Container Client = ",container_client)
        #print("Type of Container Client = ", type(container_client))  
        print("Container Created - ", c_name )

    except Exception as ex:
        print('Exception:')
        #print(ex)
    
def Container_delete(c_name):
    try:
        connect_str = "DefaultEndpointsProtocol=https;AccountName=globalmicrotel;AccountKey=wsLwVILrwM+6RKwnkqQLORiUeLozc0odFqeNZyhRexkNUWxIddDnbVuR3jN7wz2nW+/1ry6mDx+hL3WN5t35xw==;EndpointSuffix=core.windows.net"
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        container_client = blob_service_client.get_container_client(c_name)
        #print(container_client)
        #input("Press Enter to delete container")
        container_client.delete_container()
        print("Container Deleted - ", c_name )
    except Exception as ex:
        print('Exception:')
        #print(ex)
def Container_list(c_name):
    try:
        connect_str = "DefaultEndpointsProtocol=https;AccountName=globalmicrotel;AccountKey=wsLwVILrwM+6RKwnkqQLORiUeLozc0odFqeNZyhRexkNUWxIddDnbVuR3jN7wz2nW+/1ry6mDx+hL3WN5t35xw==;EndpointSuffix=core.windows.net"
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        container_client = blob_service_client.get_container_client(c_name)
        #container_client = blob_service_client.get_container_client("shailesh")
        #print("Listing blobs...")
        # List the blobs in the container
        blob_list = container_client.list_blobs()
        ls = []
        for blob in blob_list:
            blob_client = blob_service_client.get_blob_client(container=c_name, blob=blob.name)
            ls.append(blob_client.url)
        return ls
    except Exception as ex:
        print('Exception:')
        #print(ex)     
   
def upload_blob(f_name,c_name):
    try:
        connect_str = "DefaultEndpointsProtocol=https;AccountName=globalmicrotel;AccountKey=wsLwVILrwM+6RKwnkqQLORiUeLozc0odFqeNZyhRexkNUWxIddDnbVuR3jN7wz2nW+/1ry6mDx+hL3WN5t35xw==;EndpointSuffix=core.windows.net"
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        local_path = "media" 
        local_file_name = f_name
        container_name = c_name
        upload_file_path = os.path.join(local_path, local_file_name)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
        #print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)
        # Upload the created file
        with open(upload_file_path, "rb") as data:
            blob_client.upload_blob(data)
        os.remove(upload_file_path)
        return blob_client.url
        
    except Exception as ex:
        os.remove(upload_file_path)
        return "Blob Uploaded Error - File name alreday exits : "+f_name
        print(ex)       
        

def download_blob(f_name,c_name):
    try:
        connect_str = "DefaultEndpointsProtocol=https;AccountName=globalmicrotel;AccountKey=wsLwVILrwM+6RKwnkqQLORiUeLozc0odFqeNZyhRexkNUWxIddDnbVuR3jN7wz2nW+/1ry6mDx+hL3WN5t35xw==;EndpointSuffix=core.windows.net"
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        # download the blob of container
        container_name = c_name
        local_file_name = f_name
        local_path = "./media"
        downloaded_file_name = str.replace(local_file_name ,'.txt', '_web.txt')
        download_file_path = os.path.join(local_path, downloaded_file_name )
        #print("\nDownloading blob to \n\t" + download_file_path)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
        with open(download_file_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())
        print("Blob Downloaded - ", downloaded_file_name)
    except Exception as ex:
        print('Exception:')