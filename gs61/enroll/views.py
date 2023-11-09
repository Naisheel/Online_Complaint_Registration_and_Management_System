from django.shortcuts import render,HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def sign_up(request):
    if request.method== "POST":
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponse("Sign-up successful!")
    else:
        fm=UserCreationForm()
        return render(request,'enroll/signup.html',{'form':fm})      
    
