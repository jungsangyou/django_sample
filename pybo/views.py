from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.utils import timezone

from .models import Question

# Create your views here.
def index(request):
    """
    index page

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    question_list = Question.objects.order_by('-create_date')
    
    context = {'question_list' : question_list}
    
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    detail page

    Args:
        request (_type_): _description_,
        question_id : question key

    Returns:
        _type_: _description_
    """
    
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    """_summary_
        답변등록

    Args:
        request (_type_): _description_
        question_id (_type_): _description_
    """
    
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    
    return redirect('pybo:detail', question_id=question.id)
