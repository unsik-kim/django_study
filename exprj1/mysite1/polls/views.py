from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, Choice
from django.template import loader

from django.http import Http404


def index(request):
    questions = Question.objects.all()
    # return render(request, 'temp_test/index.html')

    context = {'questions': questions}
    return render(request, 'temp_test/index.html', context)
