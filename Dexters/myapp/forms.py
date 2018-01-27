from django import forms
from .models import Question, Answer, Comment, Article

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
