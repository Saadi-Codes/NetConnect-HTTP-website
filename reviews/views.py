from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse

from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
    
        return render(request, 'reviews/review.html',{
        "form": form
        })
        
    def post(self, request):
    
        form = ReviewForm(request.POST)
        
        if form.is_valid():
        #     review = Review(user_name=form.cleaned_data['user_name'], 
        #                     review_text=form.cleaned_data['review_text'], 
        #                     rating=form.cleaned_data['rating'])  
            form.save()
            thanks_url = reverse('thank_you')
            print(f"Redirecting to: {thanks_url}")  # This will print the generated URL
            return HttpResponseRedirect(thanks_url)
        
        return render(request, "reviews/review.html", {
            "form": form
        })

# def review(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
        
#         if form.is_valid():
#         #     review = Review(user_name=form.cleaned_data['user_name'], 
#         #                     review_text=form.cleaned_data['review_text'], 
#         #                     rating=form.cleaned_data['rating'])  
#             form.save()
#             return HttpResponseRedirect("/thank-you")
    
#     else:
#         form = ReviewForm()
    
#     return render(request, 'reviews/review.html',{
#         "form": form
#     })

def thank_you(request):
    print("Thank you page accessed")  # Add a print statement to check if it's called
    return render(request, "reviews/thankyou.html")

def home(request):
    return render(request, "reviews/home.html")