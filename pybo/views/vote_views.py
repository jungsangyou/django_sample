from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from pybo.models import Question, Answer

@login_required(login_url='common:login')
def vote_question(request, question_id):
    """_summary_

    Args:
        request (_type_): _description_
        question_id (_type_): _description_
    """
    
    question = get_object_or_404(Question, pk=question_id)
    
    if request.user == question.author :
        messages.error(request, '본인이 작성한 글은 추천 할 수 없습니다.')
    else:
        question.votor.add(request.user)
    return redirect('pybo:detail', question_id=question_id)


@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    """_summary_

    Args:
        request (_type_): _description_
        answer_id (_type_): _description_
    """
    
    answer = get_object_or_404(Answer, pk=answer_id)
    
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천 할 수 없습니다.')
        
    else:
        answer.votor.add(request.user)
    return redirect('pybo:detail', question_id=answer.question.id)