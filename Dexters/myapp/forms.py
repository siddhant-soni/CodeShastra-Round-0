from django import forms
from search import search_question, search_ articles
from .models import User, Question, Answer, Comment, Article, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ask_question_form(forms.ModelForm):
    # question = Question()
    # question.question = forms.TextField(label='Your Question')
    class Meta:
        model = Question
        fields = [
            "question"]

class answer_question_form(forms.ModelForm):
    # answer = Answer()
    # answer.answer = forms.TextField(label='Your Answer')
    class Meta:
        model = Answer
        fields = ["answer"]

class comment_form(forms.ModelForm):
    # comment = Comment()
    # comment.content = forms.TextField(label='Your Comment')
    class Meta:
        model = Comment
        fields = ["content"]

class publish_article_form(forms.ModelForm):
    # article = Article()
    # article.title = form.CharField(max_length=100, label='Title')
    # article.content = forms.TextField(label='Body')
    class Meta:
        model = Article
        fields = ["title","content"]

class profile_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []

<<<<<<< HEAD


=======
class search(forms.Form):
    search_field=forms.TextField(label="Search")

    for e in Article.objects.all():
        search_articles(e)
    for e in Question.objects.all():
        search_questions(e)
>>>>>>> 4560edb468d25496d6c74a54a908e29d367b2086


class registration_form(UserCreationForm):

    # user=User()
    # user.first_name=forms.CharField(label='Enter your first name')
    # user.last_name=forms.CharField(label='Enter your last name')
    # user.email_ID=forms.EmailField(label='Enter you email-ID', max_length=100)
    # user.user_name=forms.CharField(label='User Name')
    # user.password=forms.CharField(label='Enter password')
    class Meta:
        model = User
        fields = ["first_name","last_name","email","username"]
