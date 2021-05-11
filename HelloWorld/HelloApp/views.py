from django.shortcuts import render
from HelloApp.forms import FeedbackForm
# Create your views here.
def home(request):
    return render(request,'html/home.html')

def blog(request):
    return render(request,'html/blog.html')

def contact(request):
    hello=FeedbackForm() 
    if request.method=="POST":
        hello=FeedbackForm(request.POST)
        if hello.is_valid():
            hello.save()
    context={'ok':hello}

    return render(request,'html/contact.html',context)