from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ..models import Question, Choice
from ..serializers import QuestionSerializer, ChoiseSerializer


@csrf_exempt
def question_list_api(request):
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)
