from django import forms
from .models import User, Question, Answer, Comment, Article

class ask_question_form(forms.Form):
    question = Question()
    question.question = forms.TextField(label='Your Question')

class answer_question_form(forms.Form):
    answer = Answer()
    answer.answer = forms.TextField(label='Your Answer')

class comment_form(forms.Forms):
    comment = Comment()
    comment.content = forms.TextField(label='Your Comment')

class publish_article_form(forms.Forms):
    article = Article()
    article.title = form.CharField(max_length=100, label='Title')
    article.content = forms.TextField(label='Body')

class registration_form(forms.Form):
    user=User()
    user.first_name=forms.CharField(label='Enter your first name')
    user.last_name=forms.CharField(label='Enter your last name')
    user.email_ID=forms.EmailField(label='Enter you email-ID', max_length=100)
    user.user_name=forms.CharField(label='User Name')
    user.password=forms.CharField(label='Enter password')

