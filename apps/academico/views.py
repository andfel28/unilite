from django.shortcuts import render

# Create your views here.

def home(request):
    v_idOwner = 2020  # Francisco
    #return render(request,'home.html',{'idOwner':v_idOwner})
    return render(request,'home.html',{'idOwner':v_idOwner})