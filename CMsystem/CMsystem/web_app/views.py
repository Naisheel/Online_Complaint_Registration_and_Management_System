from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm,UserProfileform,UserProfileUpdateform,ProfileUpdateForm,ComplaintForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from .models import Profile,Complaint
from django.db.models import Count, Q
# Create your views here.
def index(request):
    return render(request,"CMsystem/home.html")

def aboutus(request):
    return render(request,"CMsystem/aboutus.html")

def signin(request):
    return render(request,"CMsystem/signin.html")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form=UserProfileform(request.POST)
        if form.is_valid() and profile_form.is_valid() :
            new_user=form.save()
            profile=profile_form.save(commit=False)
            if profile.user_id is None:
                profile.user_id=new_user.id
            profile.save()
            messages.add_message(request,messages.SUCCESS, f' Registered Successfully ')
            return redirect('/signin/')
    else:
        form = UserRegisterForm()
        profile_form=UserProfileform()

    context={'form': form,'profile_form':profile_form }
    return render(request, 'CMsystem/register.html',context )


@login_required
def dashboard(request):       
    if request.method == 'POST':
        p_form=ProfileUpdateForm(request.POST,instance=request.user)
        profile_update_form=UserProfileUpdateform(request.POST,request.FILES,instance=request.user.profile)
        if p_form.is_valid() and profile_update_form.is_valid():
                user=p_form.save()
                profile=profile_update_form.save(commit=False)
                profile.user=user
                profile.save()
                messages.add_message(request,messages.SUCCESS, f'Update Successfully Done')
                # return render(request,'GRsystem/dashboard.html',)
    else:
        p_form=ProfileUpdateForm(instance=request.user)
        profile_update_form=UserProfileUpdateform(instance=request.user.profile)
    context={
        'p_form':p_form,
        'profile_update_form':profile_update_form,
        }
    return render(request, 'CMsystem/dashboard.html',context)

# password reset by logging with the help of old password
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.add_message(request,messages.SUCCESS, f'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.add_message(request,messages.WARNING, f'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'CMsystem/change_password.html', {
        'form': form
    })


def complaints(request):
  
    if request.method == 'POST':
        complaint_form=ComplaintForm(request.POST)
        if complaint_form.is_valid():
               instance=complaint_form.save(commit=False)
               instance.user=request.user
               mail=request.user.email
               print(mail)
               send_mail('Hi Complaint has been Received', 'Thank you for letting us know of your concern, Have a Cookie while we explore into this matter.  Dont Reply to this mail', 'testerpython13@gmail.com', [mail],fail_silently=False)
               instance.save()
               
               messages.add_message(request,messages.SUCCESS, f'Complaint Registered!!!')
               return render(request,'CMsystem/comptotal.html',)
    else:
        complaint_form=ComplaintForm(request.POST)
    context={'complaint_form':complaint_form,}
    return render(request,'CMsystem/comptotal.html',context)

# list of all unsolved complains
def list(request):
    c=Complaint.objects.filter(user=request.user).exclude(status='1')
    result=Complaint.objects.filter(user=request.user).exclude(Q(status='3') | Q(status='2'))
    #c=Complaint.objects.all()
    args={'c':c,'result':result}
    return render(request,'CMsystem/Complaints.html',args)

#get the count of all the submitted complaints,solved,unsolved.
def counter(request):
        total=Complaint.objects.all().count()
        unsolved=Complaint.objects.all().exclude(status='1').count()
        solved=Complaint.objects.all().exclude(Q(status='3') | Q(status='2')).count()
        dataset=Complaint.objects.values('Type_of_complaint').annotate(total=Count('status'),solved=Count('status', filter=Q(status='1')),
                  notsolved=Count('status', filter=Q(status='3')),inprogress=Count('status',filter=Q(status='2'))).order_by('Type_of_complaint')
        args={'total':total,'unsolved':unsolved,'solved':solved,'dataset':dataset,}
        return render(request,"CMsystem/counter.html",args)