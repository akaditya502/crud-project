from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.
def addshow(request): 
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            db = fm.cleaned_data['dob']
            ag = fm.cleaned_data['age']
            reg = User(name=nm,email=em,dob=db,age=ag)


            reg.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})
  #this function will update the record
def updatedata(request, id):
      if request.method == 'POST':
        pi =User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
              fm.save()
      else:
        pi =User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
            
                
        return render(request,'enroll/updatestudent.html',{'form':fm}) 
      return HttpResponseRedirect('/')
  
  
  
  
  
  
  # this function will Delete
def deletedata(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
 



#  if request.method == 'POST':
#         pi = User.objects.get(pk=id)
#         fm = StudentRegistration(request.POST,instance=pi)
#         if fm.is_valid():
#             fm.save()