from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostCreation
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    p_form = PostCreation()

    ctx = {
        'nodes': Post.objects.all(),
        'p_form': p_form,
        'post_to': reverse('api:post')
    }

    return render(request, 'blog/home.html', context=ctx)


def post_detail(request, username, post_id):
    print(username)
    requested_post = get_object_or_404(Post, id=post_id)
    p_form = PostCreation()

    ctx = {
        "node": requested_post,
        "p_form": p_form,
        'post_to': reverse('api:comment-post', args=(post_id,))
    }

    return render(request, 'blog/post_detail.html', context=ctx)


def about(request):
    return render(request, 'blog/about.html', context={"title": "About"})
