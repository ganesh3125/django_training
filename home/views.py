from django.shortcuts import render,redirect
from django.contrib import messages
from home.forms import StudentSearchForm,studenteditform
from home.models import student

# Create your views here.

def home_view(request):


    if request.method=='POST':
        search=StudentSearchForm(request.POST)
        if search.is_valid():
            value=search.cleaned_data.get('q')
            result=student.objects.filter(student_name__contains=value)
            return render(request,'print_home.html',{'result':result,'form':StudentSearchForm()})

        else:
            form=StudentSearchForm()
            result=student.objects.all()
            return render(request,'print_home.html',{'form':form})



    #form=StudentSearchForm()
    #msg='hello!!!'
    #context={'form':form,'msg':msg}
    #return render(request,'home.html',context)



def contact(request):
    return render(request,'contact.html')

def deletestd(request,id):
    result=student.objects.get(id=id)
    result.delete()
    messages.success(request,'deleted succesfully!!!')
    return redirect('/')


def about(request):
    return render(request,'about.html')

def editstudent(request,id):
        request.session['id']=id
        print("request.session['id']",request.session['id'])
        student=Student.objects.get(id=id)
        if request.method=="POST":
                modelform=StudentModelForm(request.POST,instance=student)
                if modelform.is_valid():
                        modelform.save()
                        return redirect('/')
        else:
                modelform=StudentModelForm(instance=student)
                return render(request,'home_edit.html',{'form':modelform,'value':'edit'})

def createstudent(request):
    if request.method=='POST':
        form=StudentSearchForm(request.POST)
        if form.is_valid():
            student1=student.objects.Create(
                student_name=form.cleaned_data.get('student_name'),
                department=form.cleaned_data.get('department')
            )
            student.save()
            messages.success(request,'createdsuccessfully!!!!')
            return redirect('/')
        else:
            form=StudentSearchForm()
            return render(request,'create.html',{'form':form})
            