from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, Choice
from django.template import loader

from django.http import Http404


def index(request):
    questions = Question.objects.all()
    str = ''
    for question in questions:
        str += "{} 날짜 : {} <br/>".format(question.question_txt,
                                         question.pub_date)
        str += "--------------------------------<br/>"
    return HttpResponse(str)

# def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
# Create your views here.
