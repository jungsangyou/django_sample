from django.http import HttpResponse
from django.shortcuts import render

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
    
    question = Question.objects.get(id=question_id)
    
    context = {'question' : question}
    
    return render(request, 'pybo/question_detail.html', context)
