from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'rating', 'review_text', 'recommend', 'visit_again', 'created_at')  
    search_fields = ('user_name', 'review_text')
    list_filter = ('rating',)
