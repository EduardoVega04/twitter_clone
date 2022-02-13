from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from blog.models import Post, Like, Retweet
from users.models import Profile
from blog.forms import PostCreation


@require_http_methods(["POST"])
@login_required
def post(request):
    p_form = PostCreation(request.POST, request.FILES)
    if p_form.is_valid():
        new_post = p_form.save(commit=False)
        new_post.author = request.user.profile
        new_post.save()
    return redirect(reverse('blog:blog-home'))


@require_http_methods(["POST"])
@login_required
def retweet_post(request, post_id):
    requested_post = get_object_or_404(Post, id=post_id)

    retweet, created = Retweet.objects.get_or_create(
        author=request.user.profile, related_post=requested_post)

    if not created:
        retweet.delete()

    return JsonResponse({})


@require_http_methods(["POST"])
@login_required
def like_post(request, post_id):
    requested_post = get_object_or_404(Post, id=post_id)

    like, created = Like.objects.get_or_create(
        author=request.user.profile, related_post=requested_post)
    
    if not created:
        like.delete()

    return JsonResponse({})


@require_http_methods(["POST"])
@login_required
def comment_post(request, post_id):
    requested_post = get_object_or_404(Post, id=post_id)
    post_owner_username = requested_post.author.user.username

    p_form = PostCreation(request.POST, request.FILES)
    if p_form.is_valid():
        new_post = p_form.save(commit=False)
        new_post.author = request.user.profile
        new_post.parent = requested_post
        new_post.save()
    return redirect(reverse('users:post-detail', args=(post_owner_username, post_id,)))


@require_http_methods(["POST"])
@login_required
def delete_post(request, post_id):
    requested_post = get_object_or_404(Post, id=post_id)

    if requested_post.author == request.user.profile:
        requested_post.delete()
        return JsonResponse({'deleted': post_id})
    else:
        return HttpResponseForbidden()


@require_http_methods(["POST"])
@login_required
def pin_post(request, post_id):
    requested_post = get_object_or_404(Post, id=post_id)
    pinned_tweet = request.user.profile.profilefeed.pinned_tweet

    if requested_post.author != request.user.profile:
        return HttpResponseForbidden()
    else:
        if pinned_tweet != requested_post or pinned_tweet is None:
            request.user.profile.profilefeed.pinned_tweet = requested_post
        else:
            request.user.profile.profilefeed.pinned_tweet = None

    request.user.profile.profilefeed.save()
    return JsonResponse({})


@require_http_methods(["POST"])
@login_required
def follow_user(request, followee_id):
    follower = get_object_or_404(Profile, id=request.user.profile.id)
    followee = get_object_or_404(Profile, id=followee_id)

    if follower == followee:
        return HttpResponseForbidden()
    elif followee not in follower.following.all():
        follower.following.add(followee)
    else:
        follower.following.remove(followee)

    return JsonResponse({})
