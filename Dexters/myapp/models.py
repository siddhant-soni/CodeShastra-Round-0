from django.db import models
from django.db.models.fields import DateTimeField
# Create your models hereself

class User(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email_ID=models.EmailField(max_length=30, primary_key=True)
    user_name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)


class Question(models.Model):
    date=models.DateTimeField(auto_now=True)
    question=models.TextField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Answer(models.Model):
    date=DateTimeField(auto_now=True)
    answer=models.TextField(primary_key=True)
    no_of_upvotes=models.BigIntegerField(null=True)
    no_of_downvotes=models.BigIntegerField(null=True)
    user=models.ForeignKey(models.CASCADE)


class Article(models.Model):
    date=models.DateTimeField(auto_now=True)
    title=models.CharField(max_length=100, primary_key=True)
    content=models.TextField()
    no_of_upvotes=models.BigIntegerField(null=True)
    no_of_downvotes=models.BigIntegerField(null=True)
    no_of_views=models.BigIntegerField(null=True)
    user=models.ForeignKey(models.CASCADE)


class Comment(models.Model):
    date=models.DateTimeField(auto_now=True)
    content=models.TextField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_upvotes=models.BigIntegerField(null=True)
    no_of_downvotes=models.BigIntegerField(null=True)
