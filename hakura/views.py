from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.

from hakura.models import User, Post, Follow
from hakura.forms import NewPostForm, UpdateProfile

@login_required
def welcome(request):
    posts = Post.objects.all()

    users = User.objects.all()

    return render(request, "hakura/index.html", {'posts': posts, 'users': users, 'request': request})


@login_required
def createpost(request):
    if request.method == "POST":
        userpost = Post(UserID=request.user)
        form = NewPostForm(request.POST, instance=userpost)
        if form.is_valid():
            form.save()
            return redirect(welcome)
        else:
            return HttpResponse("Form not valid.")
        # form submitted, to be processed
    else:
        form = NewPostForm()
        return render(request, "hakura/createpost.html", {'form': form})


@login_required
def updateprofile(request):
    if request.method == "POST":
        usertomodify = User.objects.get(id=request.user.id)
        form = UpdateProfile(request.POST, instance=usertomodify)
        if form.is_valid():
            form.save()
            return redirect(welcome)
        else:
            return HttpResponse("Form not valid.")
        # form submitted, to be processed
    else:
        form = UpdateProfile()
        return render(request, "hakura/updateprofile.html", {'form': form})

@login_required
def userdetails(request, id):
    user = get_object_or_404(User, pk=id)
    posts = Post.objects.filter(UserID=id)
    return render(request, "hakura/userprofile.html",
                  {'user': user, 'posts': posts})


@login_required
def allusers(request):
    users = User.objects.all()
    user = {'users': users}
    return render(request, "hakura/allusers.html", user)


createuserform = modelform_factory(User, exclude=[])


def createuser(request):
    if request.method == "POST":
        form = createuserform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(allusers)
        else:
            return HttpResponse("Form not valid.")
        # form submitted, to be processed
    else:
        form = createuserform()
        return render(request, "hakura/createuser.html", {'form': form})

def logoutuser(request):
    logout(request)
    return redirect(welcome)

@login_required
def debug_followers(request):
    follows = Follow.objects.all()
    user_following = Follow.objects.filter(user_id=request.user.id)
    user_followers = Follow.objects.filter(target_id=request.user.id)
    return render(request, "hakura/debug_followers.html", {'follows': follows, 'user_following': user_following, 'user_followers': user_followers})

@login_required
def followuser(request, id):
    if request.method == "POST":
        currentuser = User.objects.get(pk=request.user.id)
        targetuser = User.objects.get(pk=id)
        if (Follow.objects.filter(user=currentuser, target=targetuser)).exists():
            return HttpResponse("You are already following this user.")
        else:
            newfollow = Follow(user=currentuser, target=User.objects.get(pk=id))
            newfollow.save()
            return HttpResponse(str("Now following"+targetuser.username))
    else:
        return redirect(welcome)

