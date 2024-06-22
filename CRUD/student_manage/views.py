from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from student_manage.models import Student
from student_manage.forms import StudentInfoForm

def list_student(request):
    students = Student.objects.all()
    context = {"students": students}        
    return render(request, "list_student.html", context)

def update_student(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == "POST":
        fm = StudentInfoForm(request.POST, instance=student)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        fm = StudentInfoForm(instance=student)
    
    context = {
        'form': fm,
        'student': student
    }
    return render(request, "update_student.html", context)

def delete_student(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == "POST":
        student.delete()
        return redirect('list_student')
    return render(request, "list_student.html")

def add_student(request):
    if request.method == "POST":
        fm = StudentInfoForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        fm=StudentInfoForm()
        context={'form': fm}
    return render(request, "add.html", context)

def search_student(request):
    if request.method == "POST":
        search = request.POST.get('output')
        students=None
        if search:
            students = Student.objects.filter(
                Q(fname__icontains=search) |
                Q(lname__icontains=search) |
                Q(email__icontains=search) |
                Q(course__icontains=search) |
                Q(phone__icontains=search)
            )
            return render(request, "list_student.html", {"students": students})
        else:
            students = Student.objects.all()
            return render(request, "list_student.html", {"students": students})
    else:
        return HttpResponse("An Error Occurred")