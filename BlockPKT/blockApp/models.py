from django.db import models 
from django.contrib.auth.models import User 
from django.db.models.deletion import SET_NULL

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='image')
    trending = models.BooleanField(default=False)
    writer = models.ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)
    slug = models.SlugField(default='slug') 

    def __str__(self):
        return self.title