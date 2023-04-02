from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ..models import Question, Choice
from ..serializers import QuestionSerializer, ChoiceSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin,DestroyModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework import generics


class QuestionListApi(CreateModelMixin, ListModelMixin, generics.GenericAPIView):
    # def post(self, request):
    #     data = JSONParser().parse(request)
    #     serializer = QuestionSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    # def get(self, request):
    #     questions = Question.objects.all()
    #     serializer = QuestionSerializer(questions, many=True)
    #     return JsonResponse(serializer.data, safe=False)
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer

    def get(self, request, *args, **kwargs):
        self.list(request, *args, **kwargs)


def question_details_api(request, pk):
    # question = get_object_or_404(Question, pk=pk)
    try:
        question = Question.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(question, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    elif request.method == 'DELETE':
        question.delete()
        return HttpResponse(status=204)


@api_view(['GET','POST'])
@csrf_exempt
def choice_list_api(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ChoiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    elif request.method == 'GET':
        choices = Choice.objects.all()
        serializer = ChoiceSerializer(choices, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET','PUT','DELETE'])
@csrf_exempt
def choice_details_api(request, pk):
    # question = get_object_or_404(Question, pk=pk)
    try:
        choice = Choice.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ChoiceSerializer(choice)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ChoiceSerializer(choice, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    elif request.method == 'DELETE':
        choice.delete()
        return HttpResponse(status=204)
