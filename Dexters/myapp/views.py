from django.shortcuts import render
from .models import User, Question, Answer, Comment
from .forms import ask_question_form, answer_question_form, comment_form, publish_article_form

# Create your views here.
def ask_question(request):
    if request.method == 'POST':
        ask_form = ask_question_form(request.POST)
        if ask_form.is_valid():
            question = ask_form.question
            question.save()
            context = {
                'question':question.question,
                'question_time':question.date,
            }
            return render(request, '', context)
    else:
        ask_form = ask_question_form()
    return render(request, '',{'ask_form':ask_form})

def answer_question(request):
    if request.method == 'POST':
        answer_form = answer_form(request.POST)
        if answer_form.is_valid():
            answer = answer_form.answer
            answer.save()
            context = {
                'answer':answer,
                'answer_time':answer.date,
                'answer_upvotes':answer.no_of_upvotes,
                'answer_downvotes':answer.no_of_downvotes,
            }
            return render(request, '', context)
    else:
        answer_form = answer_form()
    return render(request, '',{'answer_form':answer_form})

def comment(request):
    if request.method == 'POST':
        comment = comment_form(request.POST)
        if comment.is_valid():
            comment = comment_form.comment
            comment.save()
            context = {
                'comment':comment.content,
                'comment_time':comment.date,
                'comment_upvotes':comment.no_of_downvotes,
                'comment_downvotes':comment.no_of_upvotes,
            }
            return render(request, '', context)
    else:
        comment = comment_form()
    return render(request, '',{'comment':comment})

def publish_article(request):
    if request.method == 'POST':
        publish_form = publish_article_form(request.POST)
        if publish_form.is_valid():
            article = publish_article.article
            article.save()
            context = {
                'title':article.title,
                'content':article.content,
                'article_upvotes':article.no_of_upvotes,
                'article_downvotes':article.no_of_downvotes,
                'article_time':article.date,
            }
            return render(request, '', context)
    else:
        publish_article = publish_article_form()
    return render(request, '',{'ask_form':ask_form})
