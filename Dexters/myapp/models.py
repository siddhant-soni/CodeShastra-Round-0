from django.db import models
from django.db.models.fields import DateTimeField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models hereself

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #first_name=models.CharField(max_length=30)
    #last_name=models.CharField(max_length=30)
    #email_ID=models.EmailField(max_length=30, primary_key=True)
    #question=models.ForeignKey(Question, null=True)
    # user_name=models.CharField(max_length=30)
    # password=models.CharField(max_length=30)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class Tags(models.Model):
    topic=models.CharField(max_length=50)
    auto_increment_id=models.AutoField(primary_key=True)
    profile=models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.topic


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Question(models.Model):
    date=models.DateTimeField(auto_now=True)
    question=models.CharField(primary_key=True, max_length=254)
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tags)

    def __str__(self):
        return self.question

class Answer(models.Model):
    date=DateTimeField(auto_now=True)
    answer=models.CharField(primary_key=True, max_length=254)
    question=models.OneToOneField(Question, on_delete=models.CASCADE)
    no_of_upvotes=models.BigIntegerField(null=True)
    no_of_downvotes=models.BigIntegerField(null=True)
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer


class Article(models.Model):
    date=models.DateTimeField(auto_now=True)
    title=models.CharField(max_length=100, primary_key=True)
    content=models.TextField()
    no_of_upvotes=models.BigIntegerField(null=True)
    no_of_downvotes=models.BigIntegerField(null=True)
    no_of_views=models.BigIntegerField(null=True)
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tags)

    def __str__(self):
        return self.title



class Comment(models.Model):
    date=models.DateTimeField(auto_now=True)
    content=models.CharField(primary_key=True, max_length=254)
    profile=models.OneToOneField(Profile, on_delete=models.CASCADE)
    no_of_upvotes=models.BigIntegerField(null=True)
    no_of_downvotes=models.BigIntegerField(null=True)
    answer=models.ForeignKey(Answer, on_delete=models.CASCADE)
    article=models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
