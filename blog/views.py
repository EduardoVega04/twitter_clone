from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostCreation
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    p_form = PostCreation()
    user_profile = request.user.profile
    nodes = Post.objects.none()

    for follower in user_profile.following.all():
        nodes = nodes.union(
            follower.profilefeed.retweeted.all(),
            follower.profilefeed.liked.all(),
            follower.post_set.all()
        )

    ctx = {
        'nodes': nodes.order_by('-date_posted'),
        'p_form': p_form,
        'post_to': reverse('api:post')
    }

    return render(request, 'blog/home.html', context=ctx)


def post_detail(request, username, post_id):
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
