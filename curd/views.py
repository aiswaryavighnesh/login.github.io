from django.shortcuts import render
from .models import post
from django.contrib import messages


def home(request):
    posts=post.objects.all()
    return render(request,'home.html',{'posts':posts})


def add(request):
    if request.method=='POST':
        title=request.POST['title']
        detail=request.POST['detail']
        post.objects.create(title=title,detail=detail)
        messages.success(request,'Data has been added')
    return render(request,'add.html')


def update(request, id, post=None):
    if request.method=='POST':
        title=request.POST['title']
        detail=request.POST['detail']
        post.objects.filter(id=id).update(title=title,detail=detail)
        messages.success(request,'Data has been updated')
    post=post.objects.get(id=id)
    return render(request,'update.html',{'post':post})

