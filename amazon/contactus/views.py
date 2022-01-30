from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.

def contactus(request):
    Email= request.POST.get('Email')
    Comment= request.POST.get('Comment')
    submitbutton= request.POST.get('Submit')
    context={'Email': Email, 'Comment':Comment,
              'submitbutton': submitbutton}
    return render(request,'contactus/home.html',context)
# Create your views here.
