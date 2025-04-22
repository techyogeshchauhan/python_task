from django.shortcuts import render
from .models import Quote
import random

def random_quote(request):
    # Get all quotes
    quotes = Quote.objects.all()
    
    # If there are no quotes, return None
    if not quotes:
        quote = None
    else:
        # Get a random quote
        quote = random.choice(quotes)
    
    context = {
        'quote': quote,
    }
    return render(request, 'quotes/random_quote.html', context)
