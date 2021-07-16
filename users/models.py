'''Profile - BaseUser'''

from django.db import models
from django.contrib.auth.models import User;
# Create your models here.

class Profile (models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture_url = models.ImageField(blank=True, null=True)
    header_img_url = models.ImageField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    followers = models.IntegerField(blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    posts = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.user.get_full_name()