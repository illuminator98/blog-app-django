from django.db import models
from django.contrib.auth.models import User 
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.



class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age =models.IntegerField(null=True, blank=True)
    avatar=models.ImageField(default='blog_app/media/avatar.png')  

@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

class Post(models.Model):
    title=models.CharField(max_length=255)
    text=models.CharField(max_length=1023)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
   


class Comment(models.Model):
    user=models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text=models.CharField(max_length=511)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)