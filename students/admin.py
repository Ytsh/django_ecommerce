from django.contrib import admin

from students.models import College, Student

# Register your models here.

admin.site.register(College)
admin.site.register(Student)
# python manage.py createsuperuser #create a super admin
