from django.shortcuts import render, redirect
from .forms import ProductReviewForm
from .models import ProductReview

def submit_review(request):
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ProductReviewForm()
    return render(request, 'reviews/submit_review.html', {'form': form})

def review_list(request):
    reviews = ProductReview.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})
