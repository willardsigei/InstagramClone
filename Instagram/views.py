from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image, Profile,Comment,Followwww


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    posts = Image.objects.all()
    profile = Profile.objects.all()
    comments = Comment.objects.all()
    # profile = Profile.objects.filter(user=Image.profile.id).first()
    # print('posts',posts)
    return render(request,'index.html',{"posts":posts,"profile":profile,"comments":comments})
