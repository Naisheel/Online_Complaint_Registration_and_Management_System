from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,"CMsystem/home.html")

def aboutus(request):
    return render(request,"CMsystem/aboutus.html")
