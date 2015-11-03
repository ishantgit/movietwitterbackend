from django.db import models
from movie.models import Movie
 
# Create your models here.

class Tweet(models.Model):
	tweet_text = models.ForeignKey(Movie)
	tweet_polarity = models.DecimalField(null = True,blank = True, decimal_places = 20 , max_digits = 25)
	tweet_subjectivity = models.DecimalField(null = True,blank = True, decimal_places = 20 , max_digits = 25)
