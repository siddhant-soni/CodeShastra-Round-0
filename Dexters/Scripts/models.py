from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email_ID=models.EmailField(max_length=30, primary_key=True)
    user_name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)


class Question(models.Model):
    date=models.DateTimeField()
    question=models.TextField(primary_key=True)



class Answer(models.Model):
    date=DateTimeField()
    answer=models.TextField(primary_key=True)
    no_of_upvotes=models.BigIntegerField()
    no_of_downvotes=models.BigIntegerField()





class Article(models.Model):
    date=models.DateTimeField()
    title=models.CharField(max_length=100, primary_key=True)
    content=models.TextField()
    no_of_upvotes=models.BigIntegerField()
    no_of_downvotes=models.BigIntegerField()

class Comment(models.Model):
    date=models.DateTimeField()
    content=models.TextField(primary_key=True)
    user=models.ForeignKey(User)
