from django.shortcuts import render

# Create your views here.
def open_main(request):
    return render(request,'mainpage.html')

def open_thekkady(request):
    return render(request,'thekkady.html',{'dis':'heart-warming'}) 

def open_wayanad(request):
    return render(request,'wayanad.html',{'dis':'Deccan Plateau'}) 

def open_vagamon(request):
    return render(request,'vagamon.html',{'key':'Places'}) 

def open_alleppey(request):
    words={'first':'Backwater Capital of India','second':'Backwater Paradise in God’s Own Country','thrid':'Venetian Capital of Kerala','four':'Venice of the East'}
    return render(request,'alleppey.html',words)  

def open_sample (request):
    return render(request,'sample.html') 

def open_add (request):
    return render(request,'addnum.html')       

def add_num(request):
    n1=int(request.GET["num1"])
    n2=int(request.GET["num2"])
    sum=n1+n2
    return render(request,'result.html',{'result':sum})


