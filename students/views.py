# Create your views here.

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from students.forms import StudentForm
from students.models import College, Student


def students(request):
    students = Student.objects.all().values()
    template = loader.get_template("student.html")
    context = {
        'students':students
    }
    return HttpResponse(template.render(context,request))

def createStudent(request):

    if request.method == 'GET':
        # template = loader.get_template("createStudent.html")
        form = StudentForm()
        college = College.objects.all().values() #shortcut to write SQL query
        # "select * from college"
        return render(request,'createStudent.html',{'college':college, 'studentForm':form})
    elif request.method == "POST":
        # rollNo = request.POST.get('rollNo')
        # name = request.POST.get('name')
        # address = request.POST.get('address')
        # dob = request.POST.get('DOB')
        # collegeId = request.POST.get('college')
        # print(rollNo,name,address,dob,collegeId)
        form  = StudentForm(request.POST)
        if form.is_valid():
            rollNo = form.cleaned_data['rollNo']
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            dob = form.cleaned_data['DOB']
            collegeId = form.cleaned_data['college']
            print(rollNo,name,address,dob,collegeId)

            college = College.objects.get(id = collegeId)

            student = Student.objects.create(
                rollNo = rollNo,
                name = name,
                address = address,
                birth_date = dob,
                college = college
            )
            return redirect('students')
        
        
        # college =  College.objects.create(name = "Bernhardt", location = "Bafal")

        print(request)
    
        return HttpResponse("OK")

def viewStudent(request):
    students = Student.objects.all()
    return HttpResponse(students[0].__dict__)