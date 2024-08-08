
from django.urls import path

from students import views


urlpatterns = [
    path('students/', views.students, name='students'),
    path('create_student/', views.createStudent, name = 'createStudent'),
    path('view/', views.viewStudent, name = 'view')
]


# Install Django:

# pip install django

# To check django : django-admin --version

# Create a Django project:

# git clone https://github.com/django/django.git

# py -m django startproject Yourprojectname

# django-admin startproject myproject
# cd myproject

# Start the development server:
# python manage.py runserver
# py manage.py startapp students


# python manage.py makemigrations 
# # this creates a sql query to create or update
# python manage.py migrate 
# # this applied the sql query created above
# python manage.py createsuperuser #create a super admin