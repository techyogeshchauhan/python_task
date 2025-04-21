from django.shortcuts import render, redirect
from .forms import ProductReviewForm
from .models import ProductReview

def product_page(request):
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_page')  # Prevent resubmission on refresh
    else:
        form = ProductReviewForm()

    reviews = ProductReview.objects.all()
    return render(request, 'reviews/product_page.html', {'form': form, 'reviews': reviews})
