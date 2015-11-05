from django.db import models
from movie.models import Movie
 
# Create your models here.

class Tweet(models.Model):
	tweet_movie = models.ForeignKey(Movie, null = True)
	tweet_text = models.TextField(null = True ,blank = True) 
	tweet_polarity = models.DecimalField(null = True,blank = True, decimal_places = 20 , max_digits = 25)
	tweet_subjectivity = models.DecimalField(null = True,blank = True, decimal_places = 20 , max_digits = 25)
