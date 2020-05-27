from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# create our post model
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    # on_delete is used to delete the user's post when user is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
