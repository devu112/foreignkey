from django.shortcuts import render,redirect,HttpResponse
from userapp.models import course,student


# Create your views here.
def home(request):
    return render(request,'home.html')
def addcourse(request):
    return render(request,'addcourse.html')
def addstudent(request):
    course1 = course.objects.all()
    return render(request,'addstudent.html',{'course':course1})
def showdetails(request):
    student1=student.objects.all()
    return render(request,'showdetails.html',{'students':student1})
def course_db(request):
    if request.method=='POST':
        cname = request.POST['name']
        fee = request.POST['fee']
        course1 =course(coursename=cname,fee=fee)
        course1.save()
        return redirect('addcourse')
def studentdb(request):
    if request.method=='POST':
        sname = request.POST['name']
        address =request.POST['add']
        age =request.POST['age']
        jdate =request.POST['jd']
        sel =request.POST['sel']
        courses = course.objects.get(id=sel)
        student1=student(studentname=sname,address=address,age=age,joiningdate=jdate,course=courses)
        student1.save()
        return redirect('addstudent')
def edit(request,pk):
    student1=student.objects.get(id=pk)
    course1=course.objects.all()
    return render(request,'edit.html',{'s':student1, 'course':course1})
def editdb(request,pk):
    if request.method=='POST':
        student1=student.objects.get(id=pk)
        student1.studentname=request.POST['s_name']
        student1.address=request.POST['add']
        student1.age=request.POST['age']
        student1.joiningdate=request.POST['jd']
        sel=request.POST['sel']
        course1=course.objects.get(id=sel)
        student1.course=course1
        student1.save()
        return redirect('showdetails')
    return render(request,'edit.html')
def delete(request,pk):
    student1=student.objects.get(id=pk)
    student1.delete()
    return redirect('showdetails')






    