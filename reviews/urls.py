from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Home page
    path("review/", views.ReviewView.as_view(), name="review"),  # Class-based view for the form
    path("thank-you/", views.thank_you, name="thank_you"),  # Thank you page
]
