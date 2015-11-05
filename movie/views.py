from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.core import serializers
from .models import Movie
from django.http import HttpResponse
# Create your views here.
@require_GET
def getMovies(request):
	movie = Movie.objects.all()
	data = serializers.serialize('json', movie)
	return HttpResponse(data, content_type='application/json')
