from django.db import models

# Create your models here.

class MovieBase(models.Model):
	movie_name = models.CharField(primary_key = True)
	movie_genre = models.CharField(null = True)
	movie_langage = models.CharField(null = True)
	movie_imdbRating = models.CharField(null = True)
	movie_plot = models.TextFeild(null = True)
		
