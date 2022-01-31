from django.shortcuts import get_object_or_404
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
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'fail'})


@require_http_methods(["POST"])
@login_required
def retweet_post(request, post_id):
    requested_post = get_object_or_404(Post, id=post_id)

    try:
        Retweet.objects.get(author=request.user.profile).delete()
    except Retweet.DoesNotExist:
        Retweet.objects.create(related_post=requested_post, author=request.user.profile)

    return JsonResponse({})


@require_http_methods(["POST"])
@login_required
def like_post(request, post_id):
    requested_post = get_object_or_404(Post, id=post_id)

    try:
        Like.objects.get(author=request.user.profile).delete()
    except Like.DoesNotExist:
        Like.objects.create(related_post=requested_post, author=request.user.profile)

    return JsonResponse({})


@require_http_methods(["POST"])
@login_required
def comment_post(request, post_id):
    requested_post = get_object_or_404(Post, id=post_id)

    p_form = PostCreation(request.POST, request.FILES)
    if p_form.is_valid():
        new_post = p_form.save(commit=False)
        new_post.author = request.user.profile
        new_post.parent = requested_post
        new_post.save()
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'fail'})


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

    if requested_post.author is not request.user.profile:
        return HttpResponseForbidden()
    else:
        if request.user.profile.feed.pinned_tweet is None:
            request.user.profile.feed.pinned_tweet = requested_post
        else:
            request.user.profile.feed.pinned_tweet = None

    request.user.profile.feed.save()
    return JsonResponse({})


@require_http_methods(["POST"])
@login_required
def follow_user(request, followee_id):
    follower = get_object_or_404(Profile, id=request.user.profile)
    followee = get_object_or_404(Profile, id=followee_id)

    if follower == followee:
        return HttpResponseForbidden()
    elif followee not in follower.following.all():
        follower.following.add(followee)
    else:
        follower.following.remove(followee)

    return JsonResponse({})
