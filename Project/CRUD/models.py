from django.db import models

class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release_year = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.movie_name