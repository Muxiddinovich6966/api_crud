# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

User = get_user_model()

# Create your models here.
class Actors(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()





class Movie(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True,null=True)
    year = models.IntegerField(default=1920)
    actors = models.ManyToManyField(Actors,related_name='actors')
    genre = models.TextField()


    def save(self,*args,**kwargs):
        if not self.slug:
            origin_slug = slugify(self.slug)
            slug = origin_slug
            count = 0
            while Movie.objects.filter(slug=slug).exists():
                slug = f"{slug}-{count}"
                count += 1
            self.slug = slug
        super().save()

    def __str__(self):
        return self.title



class CommitMovie(models.Model):
    title = models.TextField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


