from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Tweet model to store tweets in the database
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    photo = models.ImageField(upload_to='tweets/', blank=True, null=True)  # Ensure this is correct
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update when saved

    def __str__(self):
        return f'{self.user.username}-{self.text[:20]}'
