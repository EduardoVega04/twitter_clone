from multiprocessing import context
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseForbidden
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Post
from .forms import PostCreation


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
    requested_user = get_object_or_404(User, username=username)
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
    requested_user = get_object_or_404(User, username=username)
    requested_post = get_object_or_404(Post, id=post_id)

    if request.user == requested_user:
        requested_post.delete()
        return JsonResponse({'deleted': post_id})
    else:
        return HttpResponseForbidden()


def about(request):
    return render(request, 'blog/about.html', context={"title": "About"})
