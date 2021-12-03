# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm,CommentForm,profileForm,UserUpdateForm,profileForm,RegistrationForm
from .models import Image, Profile,Comment,Followwww
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    posts = Image.objects.all()
    profile = Profile.objects.all()
    comments = Comment.objects.all()
    # profile = Profile.objects.filter(user=Image.profile.id).first()
    # print('posts',posts)
    return render(request,'index.html',{"posts":posts,"profile":profile,"comments":comments})

@login_required(login_url='/accounts/login/')
def newPost(request):
    current_user = request.user
    user_profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)        
        if form.is_valid():
            image=form.cleaned_data.get('image')
            imageCaption=form.cleaned_data.get('imageCaption')
            post = Image(image = image,imageCaption= imageCaption, profile=user_profile)
            post.savePost()
            
        else:
            print(form.errors)

        return redirect('home')

    else:
        form = NewPostForm()
    return render(request, 'newPost.html', {"form": form})
    
@login_required(login_url='/accounts/login/')    
def profile(request):
    if request.method == 'POST':

        userForm = UserUpdateForm(request.POST, instance=request.user)
        profile_form = profileForm(
            request.POST, request.FILES, instance=request.user)

        if  profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('home')

    else:
        
        profile_form = profileForm(instance=request.user)
        user_form = UserUpdateForm(instance=request.user)

        params = {
            'user_form':user_form,
            'profile_form': profile_form

        }

    return render(request, 'profile.html', params)
