from django.http import HttpResponse,HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone


# note to self: any variable in a view function that will be used in a template should absolutely be added into a
# dictionary for mapping. That said variable will be used as a template variable. Remember oo


class IndexView(generic.ListView):
    """generic.ListView displays a list of objects"""
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return last five published questions and does not display questions
         to be displayed in the future"""
         # lte stands for lesser than or equal to meaning question has to either be
         #  equal to or lesser than timezone.now() but not greater than timezone.now()
         # have a nagging feeling it is a Python dunder method just like __gt__ or __eq__ or __init__
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """generic.DetailView displays a detail page for a particular type of object"""
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # request.POST functions like a key so in case input not in choice raise KeyErorr
    except(KeyError, Choice.DoesNotExist):
        # if error redisplay question form again which resides in detail.html 
        render(request, 'polls/detail.html', {
        'question': question,
        'error_message': "You didn't select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # always return a redirect if you use POST method, therefore after vote you are redirected to the
        # results page

        # reverse function exists so you don't have to hardcode your URL in the view function,
        # like example polls/detail.html
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# commented out vote function
# used multi strings as a way to comment out a huge swathe of code
#def vote(request, question_id):
    #return HttpResponse(f'You are voting on the question {question_id}')

"""def index(request):
      render takes an http object as first argument, template name as second and a context dictionary as
     third to render a template on the site. It is a shorter way than importing HttpResponse and
     django.template.loader which would have been used like:

    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render(context, request))
    
    latest_question_list = Question.objects.order_by('-pub_date')[:5] # requesting for the 5 latest questions
    
    # the context variable acts as a dictionary that maps template variables to Python objects
    context = {'latest_question_list': latest_question_list}
   
    return render(request, 'polls/index.html', context)


  def detail(request, question_id):
     Instead of using the Model.objects.get() method together with a Model.DoesNotExist exception,
    try the from django.shortcut import get_object_or_404()
    Like this:

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', context)
    where get_object_or_404 takes a model as a first argument and a an arbitrary keyword argument which is 
    passed to the get() function of the model manager or raises 404 if object not found.

    This is actually a better approach because the Model/Object.DoesNotExist error couples the model layer 
    tightly with the view layer. The get_object_or_404 decouples it. 
    There is also get_list_or_404() which works like get_object_or_404 but with a filter() instead of get() instead
    It raises a 404 if list is empty
    
    try:
        question = Question.objects.get(pk=question_id)
        context = {'question': question} 
    except Question.DoesNotExist:
        return Http404('Question does not exist')
    return render(request, 'polls/detail.html/', context)

# commented out results function which was created at early, primitive stages
#def results(request, question_id):
    #response = f'You are looking at the results of {question_id}'
    #return HttpResponse(response)


#def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    render(request, 'polls/results.html', {'question': question})"""

# Create your views here.
