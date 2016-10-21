from django.contrib import admin

# Register your models here.
from .models.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'review_count')
    search_fields = ('name','user_id',)

class BusinessAdmin(admin.ModelAdmin):
    list_display = ('business_id', 'name', 'city', 'star', 'review_count')
    search_fields = ('name','business_id',)
    list_filter = ('city',)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'business_id', 'star')
    search_fields = ('user_id','business_id',)
class CheckinAdmin(admin.ModelAdmin):
    list_display = ('business_id', 'avg_rating', 'customer_flow', 'avg_ratings')

admin.site.register(User_yelp, UserAdmin)
admin.site.register(Business, BusinessAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(CheckIn)
admin.site.register(Checkin_analysis, CheckinAdmin)
