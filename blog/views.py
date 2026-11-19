
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Post
from django.views.decorators.http import require_POST
from .forms import CommentForm

def PostList(request):

    post_list = Post.published.select_related('author').all()

    paginator = Paginator(post_list, 3)

    page_number = request.GET.get('page', 1)

    posts = paginator.get_page(page_number)

    return render(
        request,
        'blog/posts/list.html',
        {'posts': posts}
    )


def detailList(request, slug):

    post = get_object_or_404(
        Post.published.select_related('author'),
        slug=slug
    )

    return render(
        request,
        'blog/posts/detail.html',
        {'post': post}
    )
@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'blog/posts/comment.html', {'post': post, 'form': form, 'comment': comment})



