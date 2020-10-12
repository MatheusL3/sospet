from django.contrib.auth.models import User
from django.db import models


class PlacesManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            title__icontains=query, description__icontains=query
        )


class Places(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='places', verbose_name='Imagens')
    objects = PlacesManager()

    def __str__(self):
        return str(self.title)

    class Meta:
        db_table = 'places'
