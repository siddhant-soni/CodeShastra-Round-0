from django.shortcuts import render
from .models import User, Question, Answer, Comment
from .forms import ask_question_form, answer_question_form, comment_form, publish_article_form, registration_form, profile_form
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Create your views here.
@login_required
def ask_question(request):
    # if request.method == 'POST':
    #     ask_form = ask_question_form(request.POST)
    #     if ask_form.is_valid():
    #         question = ask_form.question
    #         question.save()
    #         context = {
    #             'question':question.question,
    #             'question_time':question.date,
    #         }
    #         return render(request, '', context)
    # else:
    #     ask_form = ask_question_form()
    # return render(request, '',{'ask_form':ask_form})
    ask_form = ask_question_form(request.POST or None)
    if ask_form.is_valid():
        question = ask_form.save(commit="False")
        question.save()
    context = {'ask_form':ask_form}
    return render(request, '',context)
@login_required
def answer_question(request):
    # if request.method == 'POST':
    #     answer_form = answer_question_form(request.POST)
    #     if answer_form.is_valid():
    #         answer = answer_form.answer
    #         answer.save()
    #         context = {
    #             'answer':answer.answer,
    #             'answer_time':answer.date,
    #             'answer_upvotes':answer.no_of_upvotes,
    #             'answer_downvotes':answer.no_of_downvotes,
    #         }
    #         return render(request, '', context)
    # else:
    #     answer_form = answer_question_form()
    # return render(request, '',{'answer_form':answer_form})
    answer_form = answer_question_form(request.POST or None)
    if answer_form.is_valid():
        answer = answer_form.save(commit="False")
        answer.save()
    context = {'answer_form':answer_form}
    return render(request, '',context)
@login_required
def comment(request):
    # if request.method == 'POST':
    #     comment = comment_form(request.POST)
    #     if comment.is_valid():
    #         comment = comment_form.comment
    #         comment.save()
    #         context = {
    #             'comment':comment.content,
    #             'comment_time':comment.date,
    #             'comment_upvotes':comment.no_of_downvotes,
    #             'comment_downvotes':comment.no_of_upvotes,
    #         }
    #         return render(request, '', context)
    # else:
    #     comment = comment_form()
    # return render(request, '',{'comment':comment})
    comments = comment_form(request.POST or None)
    if comment_form.is_valid():
        comments = comment_form.save(commit="False")
        comments.save()
    context = {'comment_form':comment_form}
    return render(request, '',context)
@login_required
def publish_article(request):
    # if request.method == 'POST':
    #     publish_form = publish_article_form(request.POST)
    #     if publish_form.is_valid():
    #         article = publish_form.article
    #         article.save()
    #         context = {
    #             'title':article.title,
    #             'content':article.content,
    #             'article_upvotes':article.no_of_upvotes,
    #             'article_downvotes':article.no_of_downvotes,
    #             'article_time':article.date,
    #         }
    #         return render(request, '', context)
    # else:
    #     publish_article = publish_article_form()
    # return render(request, '',{'publish_article':publish_article})
    publish_form = publish_article_form(request.POST or None)
    if publish_form.is_valid():
        article = publish_form.save(commit="False")
        article.save()
    context = {'publish_form':publish_form}
    return render(request, 'article.html',context)

def reg_form(request):
    # if request_method == 'POST':
    #     registration_form = registration_form(request.POST)
    #     if registration_form.is_valid():
    #         user=registration_form.user
    #         user.save()
    #         context = {
    #             'first_name':user.first_name,
    #             'last_name':user.last_name,
    #             'email_ID':user.email_ID,
    #             'user_name':user.user_name,
    #             'password':user.password,
    #         }
    #         return render(request, '', context)
    # else:
    #     registration_form = registration_form()
    # return render(request, '',{'registration_form':registration_form})
    user_registration_form = registration_form(request.POST or None)
    user_profile_form = profile_form(request.POST or None)
    if user_registration_form.is_valid() and user_profile_form.is_valid():
        registered_user = user_registration_form.save(commit="False")
        registered_user.save()
        registered_user.refresh_from_db()
        user_profile_form = profile_form(request.POST, instance=user.profile)
        user_profile_form.full_clean()
        user_profile_form.save()
    context = {
        'registration_form':user_registration_form,
        'profile_form':user_profile_form,
    }
    return render(request, 'registration.html',context)
def logout(request):
    auth.logout(request)
    return render(request, 'logout.html',context)
