# MyCloudBox_Project
MyCloudBox_Project
t's a sample application to store your data to cloud like dropbox, It's designed using Pyhton DJango & Azure cloud Services Steps to use this Project:

create a virtual environment. 
install dependencies using requirement.txt create a storage account in Azure Cloud & copu the connection string. 
select the database you want to link. 
edit the crediential of your database in setting.py file. 
after updating the database crediential you need to do the migration.
Update the connection staring in View.py file with correct connection string.
5(a) > python manage.py makemigrations 
5(b) > Python manage.py migrate 
run the project using python manage.py runserver see the output on http://127.0.0.1:8000/
