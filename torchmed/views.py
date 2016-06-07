from django.shortcuts import render
from django.utils.translation import activate

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # activate('pt-br')
    # print(request.LANGUAGE_CODE)
    context = {}
    return render(request, 'index.html', context)
