from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    review_count = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Business(models.Model):
    business_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=10)
    review_count = models.CharField(max_length=10)
    star = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Review(models.Model):
    user_id = models.CharField(max_length=30)
    business_id = models.CharField(max_length=30)
    star = models.CharField(max_length=10)
    date = models.CharField(max_length=20)

    def __str__(self):
        return str(self.user_id)+','+str(self.business_id)

class CheckIn(models.Model):
    business_id = models.CharField(max_length=30)
    checkin_info = models.CharField(max_length=100)

    def __str__(self):
        return self.business_id

class Checkin_analysis(models.Model):
    business_id = models.CharField(max_length=30)
    customer_flow = models.CharField(max_length=30)
    avg_rating = models.CharField(max_length=30)
    avg_ratings = models.CharField(max_length=100)

    def __str__(self):
        return self.business_id