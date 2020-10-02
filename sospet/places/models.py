from django.contrib.auth.models import User
from django.db import models


class Places(models.Model):
    title = models.CharField( max_length=100),
    slug = models.SlugField(),
    description = models.TextField(blank=True),
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True),
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='places', verbose_name='Imagens')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'places'
