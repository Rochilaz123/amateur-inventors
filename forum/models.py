from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField


PROGRESS = ((0, "Still an Idea"), (1, "Working on prototypes"), (2, "Ready for production"), (3, "This idea is now a reality!"),)

# Create your models here.
class Idea(models.Model):
    """
    Stores a single idea entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ideas"
    )
    purpose = models.TextField()
    mockup_image = CloudinaryField('image', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    details = models.TextField()
    issues = models.TextField(blank=True)
    progress = models.IntegerField(choices=PROGRESS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)