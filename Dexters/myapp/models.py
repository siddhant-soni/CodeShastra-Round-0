from django.db import models
from django.db.models.fields import DateTimeField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models hereself

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email_ID=models.EmailField(max_length=30, primary_key=True)
    # user_name=models.CharField(max_length=30)
    # password=models.CharField(max_length=30)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Question(models.Model):
    date=models.DateTimeField(auto_now=True)
    question=models.TextField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Answer(models.Model):
    date=DateTimeField(auto_now=True)
    answer=models.TextField(primary_key=True)
    no_of_upvotes=models.BigIntegerField(null=True)
    no_of_downvotes=models.BigIntegerField(null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)


class Article(models.Model):
    date=models.DateTimeField(auto_now=True)
    title=models.CharField(helptext="helptext",max_length=100, primary_key=True)
    content=models.TextField()
    no_of_upvotes=models.BigIntegerField(null=True)
    no_of_downvotes=models.BigIntegerField(null=True)
    no_of_views=models.BigIntegerField(null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    date=models.DateTimeField(auto_now=True)
    content=models.TextField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_upvotes=models.BigIntegerField(null=True)
    no_of_downvotes=models.BigIntegerField(null=True)
