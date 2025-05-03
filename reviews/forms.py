from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     user_name = forms.CharField(max_length=100, label='Your Name', error_messages={
#         "required": "Your name must not be empty",
#         "max_length" : "Please enter a shorter name.",
#     })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=500)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'  # ['user_name','review_text','rating'] or exclude = ['some_field']
        labels = {
            "user_name": 'Your Name',
            "email": 'Email Address',
            "review_text": "Your Feedback",
            "rating": "Rating",
            "recommend": "Would you recommend us?",
            "visit_again": "Would you visit again?",
        }
        error_messages = {
            "user_name": {
                "required": "Please enter your name.",
                "max_length": "Enter a shorter name.",
            },
            "email": {
                "required": "Email is required.",
                "invalid": "Enter a valid email address.",
            },
        }