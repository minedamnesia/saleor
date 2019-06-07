from django.conf import settings
from django.db import models


class Story(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='story_images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'
