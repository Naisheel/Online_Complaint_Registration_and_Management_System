from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def sign_up(request):
    if request.method== "POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            
            fm.save()
            return HttpResponse("Sign-up successful!")
    else:
        fm=SignUpForm()

        return render(request,'enroll/signup.html',{'form':fm})      
    
