from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.http import HttpResponse

from .models import Question

def index(request):
   latest_question_list = Question.objects.all()
   #return HttpResponse('Estas en la pagina principal')
   return render(request, 'polls/index.html', context={
      "latest_question_list": latest_question_list
   })

def detail(request, question_id):
   #return HttpResponse(f"Estas Viendo la preguna numero {question_id}")
   #question = Question.objects.get(pk=question_id)
   question = get_object_or_404(Question, pk=question_id)
   return render(request, 'polls/detail.html', context={
      "question": question
   })

def result(request, question_id):
   return HttpResponse(f"Estas Viendo los resultados de la pregunta numero {question_id}")

def vote(request, question_id):
   return HttpResponse(f"Estas votando a la pregunta numero {question_id}")