from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseForbidden
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Post
from .forms import PostCreation
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if request.method == 'POST':
        p_form = PostCreation(request.POST, request.FILES)
        if p_form.is_valid():
            new_post = p_form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect(reverse('blog:blog-home'))
    else:
        p_form = PostCreation()

    ctx = {
        'nodes': Post.objects.all(),
        'p_form': p_form
    } 

    return render(request, 'blog/home.html', context=ctx)


def post_detail(request, username, post_id):
    requested_post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        p_form = PostCreation(request.POST, request.FILES)
        if p_form.is_valid():
            new_post = p_form.save(commit=False)
            new_post.author = request.user
            new_post.parent = requested_post
            new_post.save()
            return redirect(request.path)
        else:
            ctx = {
                "node": requested_post,
                "p_form": p_form
            }
            return render(request, 'blog/post_detail.html', context=ctx)
    else:
        p_form = PostCreation()

    ctx = {
        "node": requested_post,
        "p_form": p_form
    }

    return render(request, 'blog/post_detail.html', context=ctx)


@require_http_methods(["POST"])
def delete_post(request, username, post_id):
    requested_post = get_object_or_404(Post, id=post_id)

    if requested_post.author == request.user:
        requested_post.delete()
        return JsonResponse({'deleted': post_id})
    else:
        return HttpResponseForbidden()


@require_http_methods(["POST"])
def pin_unpin_tweet(request, username, post_id):
    requested_post = get_object_or_404(Post, id=post_id)

    if requested_post not in request.user.post_set.all():
        return HttpResponseForbidden()
    elif requested_post in request.user.post_set.all():
        request.user.pinned_tweet = requested_post
    else:
        request.user.pinned_tweet = None

    return JsonResponse({})


@login_required
def follow_user(request, followee):
    follower = get_object_or_404(User, id=request.user.id)
    followee = get_object_or_404(User, username=followee)

    if follower == followee:
        return HttpResponseForbidden()
    elif followee.profile not in follower.profile.following.all():
        follower.profile.following.add(followee.profile)
    else:
        follower.profile.following.remove(followee.profile)

    return JsonResponse({})


def about(request):
    return render(request, 'blog/about.html', context={"title": "About"})
