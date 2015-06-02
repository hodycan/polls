from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Question, Choice

# def index(request):
#     questions = Question.objects.all()
#     context = RequestContext(request, {
#         'questions': questions,
#     })
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist.")
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'questions'    # the variable in template html

    def get_queryset(self):
        """Return all the questions"""
        return Question.objects.all()



class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'



class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question': p,
            'error_message': "You didn't select a choice."
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # redirect prevents data from being posted twice.
        # reverse returns the correct URL (without hardcoding)
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

