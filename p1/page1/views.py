from django.shortcuts import render, HttpResponse , redirect,get_object_or_404
from page1.forms import RegistrationForm, EditProfileForm
#from page1.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from page1.models import WorkerProfile
from page1.forms import Workersreg
from django.core.mail import send_mail
from django.conf import settings
from page1.models import Category
from django.core.mail import send_mail

def home(request):
    return render(request,'page1/home.html')
def appointment(request):
            ca=Category.objects.all()
            return render(request,'page1/appointment.html',{'ca':ca})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/page1/login/')
    else:
        form = RegistrationForm()

    args = {'form': form}
    return render(request, 'page1/reg.html', args)  
def login(request):
    return render(request,'/page1/profile.html')
def view_profile(request):
    args = {'user': request.user}        
    return render(request,'page1/profile.html', args)
def edit_profile(request):
    if request.method == 'post':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/page1/profile')
    else:
        form = EditProfileForm(instance=request.user)        
        args = {'form': form}
        return render(request, 'page1/edit_profile.html', args)
def change_password(request):
    if request.method == 'post':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/page1/profile')
    else:
            form = PasswordChangeForm(user=request.user)
            args = {'form': form}
            return render(request,'page1/change_password.html', args)


def Workers_registration(request):
    if request.method=='POST':
        form = Workersreg(request.POST,request.FILES)
        if form.is_valid():
            p=form.save(commit=False)
            p.user=request.user
            p.save()
            return HttpResponseRedirect('/page1')
               
        else:
            return HttpResponseRedirect('/page1')

    else:
        form = Workersreg()
        args={'form':form}
        return render(request,'page1/Workers_registration.html',args)


def send_conf(request,id):
    post= get_object_or_404(WorkerProfile, id=id)
    print(post)
    name = post.name
    phone = post.phone_number
    det = 'Name :'+name+' Phone:'+phone
    send_mail (
        'Confirmation mail',
        'Your Booking was successful.Pls contact the service representative\
        here'+det,
        'peddi.vinil@gmail.com',
        ['satyashodhaka66@gmail.com'],
        fail_silently = False,
    )
    return render(request, 'page1/filter.html', {'post':post})
class WregForm(ModelForm):
    class Meta:
        model = WorkerProfile
        fields = [
		 'name',
		'category',
		#'Jobtitle',
		'phone_number',
		
		 
		 ]

#def mail(request):  
 #   name=request.user.first_name
  #  send_mail('thank you',name,'peddi.vinil@gmail.com',['rstar735@gmail.com',],fail_silently=False)
   # return render(request,'page1/filter.html')
