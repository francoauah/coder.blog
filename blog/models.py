from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    # slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextField(blank=True, null=True)
    # content = models.TextField()
    image = models.ImageField (null=True, blank= True, upload_to = 'images/')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

#---------------------------------------------------------------------------------------#

class Profile (models.Model):
    user=models.OneToOneField(User,null=True, on_delete= models.CASCADE)
    biographie= models.TextField()
    profile_pic = models.ImageField (null=True, blank= True, upload_to = 'images/')
    twitter = models.CharField(max_length=200,null=True,blank=True)
    facebook = models.CharField(max_length=200,null=True,blank=True)
    website = models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('home')