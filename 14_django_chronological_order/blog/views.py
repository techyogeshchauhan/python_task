from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from .models import Post
from .forms import PostForm

def post_list(request):
    try:
        posts = Post.objects.all().order_by('-created_at')
        return render(request, 'blog/post_list.html', {'posts': posts})
    except Exception as e:
        messages.error(request, f"Error loading posts: {str(e)}")
        return render(request, 'blog/post_list.html', {'posts': []})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                post = form.save(commit=False)
                post.author = request.user
                post.created_at = timezone.now()
                post.save()
                messages.success(request, 'Post created successfully!')
                return redirect('post_list')
            except Exception as e:
                messages.error(request, f"Error creating post: {str(e)}")
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

def post_detail(request, pk):
    try:
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})
    except Exception as e:
        messages.error(request, f"Error loading post: {str(e)}")
        return redirect('post_list')
