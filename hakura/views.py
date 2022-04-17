from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# Create your views here.

from hakura.models import User, Post

def welcome(request):
    return HttpResponse("Welcome to Hakura Cloud.")

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