from django.shortcuts import render
from Registration.models import Course,Student
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    return render(request,'index.html')

def new_course(request):
    if request.method =='POST':
        c_code = request.POST['code']
        c_desc = request.POST['desc']
        data = Course(code=c_code,description=c_desc)
        data.save()
        return render(request, 'new_course.html',{'message':'Data Save'})
    else:
        return render(request, 'new_course.html')
    
def course(request):
    allcourse=Course.objects.all()
    dict={
        'allcourse':allcourse
    }
    return render (request,'course.html',dict)

def search_course(request):
    if request.method == 'GET':
        data = Course.objects.filter(code= request.GET.get('c_code'))
        dict = {
            'data':data
        }
        return render(request, 'search_course.html',dict)
    else:
        return render(request,'search_course.html')
    
def update_course(request,code):
    data = Course.objects.get(code=code)
    dict = {
        'data':data
    }
    return render(request,"update_course.html",dict)

def save_update_course(request,code):
     c_desc = request.POST['description']
     data = Course.objects.get(code=code)
     data.description=c_desc
     data.save()
     return HttpResponseRedirect(reverse('course'))

def delete_course(request,code):
     data = Course.objects.get(code=code)
     data.delete()
     return HttpResponseRedirect(reverse('course'))
 
#student
def new_student(request):
    #baca dari database,dict hantar ke html
    course=Course.objects.all()
    if request.method == 'POST':
        #GET data from html page (new student)
        Id = request.POST['Id']
        Name = request.POST['Name']
        Address = request.POST['Address']
        Phone = request.POST['Phone']
        S_code = request.POST['s_course']
        
        
        
        #get fk from references table
        data_course = Course.objects.get(code=S_code)
        
        #assign value data
        data= Student(id=Id,name=Name,address=Address,phone=Phone,course_code=data_course)
        
        #save data
        data.save()
        
        dict = {
            'Course': course,
            'message':"Data Save"
        }
        
    else:
        dict={
            'course': course
        }
    return render(request,'new_student.html',dict)

# by student
def searchbystudent(request):
    if request.method =='POST':
        Id= request.POST['id']
        student_data = Student.objects.get(id=Id)
        course_data = Course.objects.get(code=student_data.course_code_id)
        dict = {
            'student_data':student_data,
            'course_data':course_data,
            'message':'datasend'
        }
        return render(request,'searchbystudent.html',dict)
    else:
        return render(request,'searchbystudent.html')
    
def search_by_course(request):
    value = Course.objects.all()
    if request.method =='GET':
        list_student = Student.objects.filter(course_code=request.GET.get('s_course'))
        dict={
            'list_student':list_student,
            'value':value,
        }
        return render(request,'search_by_course.html',dict)
    else:
        
        dict = {
            'value':value,
        }
        return render(request,'search_by_course.html',dict)