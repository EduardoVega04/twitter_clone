from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.template import context
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)   # Internally create a form with the input data
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')    # cleaned_data contains the form validated data
            messages.success(request, f'Account created for {username}!')
            return redirect(reverse('login'))
    else:
        form = UserRegisterForm()   # Create a blank form

    return render(request, 'users/register.html', {'form': form})


def profile(request, username):
    requested_profile = get_object_or_404(User, username=username)
    tweets = requested_profile.post_set.all()

    ctx = {
        'requested_profile': requested_profile,
        'nodes': tweets,
        'total_tweets': len(tweets)
    }

    return render(request, 'users/profile.html', context=ctx)


def profileUpdate(request, username):
    requested_profile = get_object_or_404(User, username=username)

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=requested_profile)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=requested_profile.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect(reverse('users:profile', args=(requested_profile.username,)))
    else:
        u_form = UserUpdateForm(instance=requested_profile)
        p_form = ProfileUpdateForm(instance=requested_profile.profile)

    ctx = {
        'u_form': u_form,
        'p_form': p_form,
        'requested_profile': requested_profile
    }

    return render(request, 'users/updateProfile.html', ctx)
