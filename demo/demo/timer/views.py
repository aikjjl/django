from django.shortcuts import render

# Create your views here.

def timer(request):
    import time

    ctime=time.time()

    return render(request,"time.html",{"data":ctime})