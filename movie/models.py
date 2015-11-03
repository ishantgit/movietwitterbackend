from django.db import models

# Create your models here.

class Movie(models.Model):
	movie_name = models.CharField(primary_key = True, max_length = 100)
	movie_genre = models.CharField(null = True , default = 'n/a',max_length = 200)
	movie_langage = models.CharField(null = True, default = 'n/a', max_length = 200)
	movie_imdbRating = models.CharField(null = True, default = 'n,a', max_length = 200)
	movie_plot = models.TextField(null = True, default = 'n/a')
	movie_actor = models.CharField(null = True, default = 'n/a', max_length = 200)
	movie_writer = models.CharField(null = True, default = 'n/a', max_length = 200)
	movie_director = models.CharField(null = True, default = 'n/a',max_length = 200)
	movie_poster = models.CharField(null = True,max_length = 200)
		
