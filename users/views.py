from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Q
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
    requested_user = get_object_or_404(User, username=username)
    pinned_tweet = requested_user.profile.profilefeed.pinned_tweet

    if pinned_tweet:
        tweets = requested_user.profile.post_set.filter(~Q(id=pinned_tweet.id))
    else:
        tweets = requested_user.profile.post_set.all()

    ctx = {
        'requested_profile': requested_user.profile,
        'nodes': tweets,
        'node': pinned_tweet
    }

    return render(request, 'users/profile.html', context=ctx)


def profileUpdate(request, username):
    requested_user = get_object_or_404(User, username=request.user.username)

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=requested_user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=requested_user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect(reverse('users:profile', args=(requested_user.username,)))
    else:
        u_form = UserUpdateForm(instance=requested_user)
        p_form = ProfileUpdateForm(instance=requested_user.profile)

    ctx = {
        'u_form': u_form,
        'p_form': p_form,
        'requested_profile': requested_user.profile
    }

    return render(request, 'users/updateProfile.html', ctx)
