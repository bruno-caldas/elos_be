from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
from .models import Document, EspecieAnimal
from .forms import DocumentForm

# import datetime

class IndexView(generic.ListView):
    template_name = 'cadastro/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'cadastro/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'cadastro/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'cadastro/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('cadastro:results', args=(question.id,)))

# https://stackoverflow.com/questions/5871730/how-to-upload-a-file-in-django
def mural_animais(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'],
                            nome_cachorro=request.POST["nome"],
                            porte_cachorro=request.POST["porte"],
                            idade_cachorro=request.POST["idade"],
                            # dia_do_cadastro=datetime.date.today()
                            )
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('cadastro:mural_animais'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    especies = EspecieAnimal.objects.all()

    # Render list page with the documents and the form
    return render(request,
        'cadastro/form.html',
        {'documents': documents,'especies': especies,'form': form})
