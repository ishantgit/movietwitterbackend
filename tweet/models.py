from django.db import models
from movie.models import Movie
 
# Create your models here.

class Tweet(models.Model):
	tweet_text = models.ForeignKey(Movie)
	tweet_sentiment = models.DecimalField(null = True,blank = True, decimal_places = 5 , max_digits = 5)
