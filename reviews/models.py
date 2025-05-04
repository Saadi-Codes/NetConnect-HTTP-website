from django.db import models

# Create your models here.

class Review(models.Model):
    user_name = models.CharField(max_length=100, blank= False, null= False)
    email = models.EmailField(blank= False, null= False)
    review_text = models.TextField(blank= True, null= True)
    rating = models.IntegerField(default= 5 )
    recommend = models.BooleanField(default=True)
    visit_again = models.CharField(
        max_length=20,
        choices=[('yes', 'Yes'), ('no', 'No'), ('maybe', 'Maybe')],
        default='maybe'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user_name} - {self.rating} Stars"