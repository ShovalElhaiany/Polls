from ..models import Question
from django.views import View, generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from ..forms import QuestionForm, ChoiceForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

# class Q(generic.CreateView):
#     model=Question
#     fields= ['question_text', 'pub_date']

# class Index(LoginRequiredMixin, generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = "latest_question_list"

#     def get_queryset(self):
#         return Question.objects.order_by('-pub_date')
#         # [:5]

# class Detail(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     # question = Question.objects.get(pk=question_id)
#     return render(request=request, template_name='polls/detail.html', context={'question': question})


class Index(View):
    def get(self, request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        # output = ', '.join([q.question_text for q in latest_question_list])

        view_count = request.COOKIES.get('view_count')
        context = {"latest_question_list": latest_question_list,
                   'view_count': view_count}

        # request.session['view_count'] = view_count + 1
        resp = render(request=request, template_name='polls/index.html', context=context)
        resp.set_cookie('view_count', view_count + 1)
        return resp


class Detail(View):
    def get(self, request, question_id):
        # # into session
        # request.session['username'] = ''
        # # get from session
        # key = request.session['username']
        # key = request.session.get('username', 0)
        # # delete from session
        # del request.session['username']

        un = request.session.pop('username', 'guest')
        session_username = request.session.get('username', 'no one')
        expiratin = request.session.get_expiry_age()
        expiratin = request.session.get_expiry_date()
        request.session.set_expiry(60)
        expiratin = request.session.get_expiry_age()
        # request.session.flush()

        # if request.user.is_authenticated:
        question = get_object_or_404(Question, pk=question_id)
        return render(request=request, template_name='polls/detail.html', context={'question': question})
        # else:
        #     return HttpResponseRedirect(reverse('polls:login'))


class NewQuestion(View):
    def post(self, request):
        form = QuestionForm(request.POST)
        if form.is_valid():
            question_text = form.cleaned_data['question_text']
            pub_date = form.cleaned_data['pub_date']
            # q = Question(question_text, pub_date)
            # q.save()
            Question.objects.create(
                question_text=question_text, pub_date=pub_date)
            return HttpResponseRedirect(reverse('polls:index'))
        else:
            error_message = 'Validation failed!'
            return render(request=request, template_name='polls/question_form.html', context={'form': form, 'message': error_message})

    def get(self, request):
        form = QuestionForm()
        return render(request=request, template_name='polls/question_form.html', context={'form': form})


class NewChoice(View):
    def post(self, request):
        form = ChoiceForm(request.POST)
        if form.is_valid():
            # choice_text = form.cleaned_data['choice_text']
            # votes = form.cleaned_data['votes']
            # question = form.cleaned_data['question']
            # # q = Question(question_text, pub_date)
            # # q.save()
            # Choice.objects.create(choice_text=choice_text,votes=votes, question=question)
            form.save()
            return HttpResponseRedirect(reverse('polls:index'))

    def get(self, request):
        form = ChoiceForm()
        return render(request=request, template_name='polls/choice_form.html', context={'form': form})


class Vote (View):
    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        choice = question.choice_set.get(pk=request.POST['choice'])
        choice.votes = choice.votes + 1
        choice.save()
        return HttpResponseRedirect(reverse('polls:detail', args={question_id}))

    def get(self, request):
        return HttpResponse("THIS WAS A GET REQUEST")
