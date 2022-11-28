from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=150, blank=True, null=True)
    movie_id = models.IntegerField()
    overview = models.TextField()
    
    def __str__(self):
        return self.title

class TV(models.Model):
    name = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    tv_id = models.IntegerField()
    
    def __str__(self):
        return self.name

class MovieProvider(models.Model):
    provider_name = models.CharField(max_length=100)
    logo_path = models.CharField(max_length=150, blank=True, null=True)
    provider_id = models.IntegerField()

    def __str__(self):
        return self.provider_name

class TVProvider(models.Model):
    provider_name = models.CharField(max_length=100)
    logo_path = models.CharField(max_length=150, blank=True, null=True)
    provider_id = models.IntegerField()

    def __str__(self):
        return self.provider_name

class SearchMulti(models.Model):
    title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=150, blank=True, null=True)
    multi_id = models.IntegerField()
    overview = models.TextField()
    media_type = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class MovieDetail(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=150, blank=True, null=True)
    overview = models.TextField()
    release_date = models.CharField(max_length=100)
    runtime = models.IntegerField()
    genres = models.CharField(max_length=100)


class TVDetail(models.Model):
    tv_id = models.IntegerField()
    name = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=150, blank=True, null=True)
    overview = models.TextField()
    genres = models.CharField(max_length=100)


