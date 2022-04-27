from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# Create your views here.

from hakura.models import User, Post
from hakura.forms import NewPostForm

def welcome(request):
    posts = Post.objects.all()
    post = {'posts': posts}
    return render(request, "hakura/index.html", post)

def createpost(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(welcome)
        else:
            return HttpResponse ("Form not valid.")
        #form submitted, to be processed
    else:
        form = NewPostForm()
        return render(request, "hakura/createpost.html", {'form':form})

def userdetails(request,id):
    user = get_object_or_404(User,pk=id)
    return render(request, "hakura/userprofile.html",
                  {'user': user})

def allusers(request):
    users = User.objects.all()
    user = {'users':users}
    return render(request, "hakura/allusers.html",user)

createuserform = modelform_factory(User, exclude=[])
def createuser(request):
    if request.method == "POST":
        form = createuserform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(allusers)
        else:
            return HttpResponse ("Form not valid.")
        #form submitted, to be processed
    else:
        form = createuserform()
        return render(request, "hakura/createuser.html", {'form':form})