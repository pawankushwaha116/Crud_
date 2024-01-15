from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your Add_Show here.

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            en = fm.cleaned_data['enrollment']
            pw = fm.cleaned_data['password']
            dt = fm.cleaned_data['date']
            reg = User(name=nm, email=em, enrollment=en, password=pw, date=dt)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
        
 # Pagination Section
 
    stut_list = User.objects.all()
    paginator = Paginator(stut_list, 4)  # Show 4 students per page

    page = request.GET.get('page')
    try:
        stut = paginator.page(page)
    except PageNotAnInteger:
        
        # If page is not an integer, deliver first page.
        
        stut = paginator.page(1)
    except EmptyPage:
        
        # If page is out of range (e.g. 9999), deliver last page of results.
        
        stut = paginator.page(paginator.num_pages)

    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stut})

# Upadte/edit section here..

def update_data(request, id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)

    return render(request, 'enroll/updatestudent.html', {'form':fm})

# delete section here..

def delete_data(request, id):
    if request.method =="POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
