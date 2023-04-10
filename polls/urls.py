from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<int:question_id>/', views.Detail.as_view(), name='detail'),
    path('<int:question_id>/vote/', views.Vote.as_view(), name='vote'),
    path('newq/', views.NewQuestion.as_view(), name='newquestion'),
    path('newc/', views.NewChoice.as_view(), name='newchoice'),
    path('register/', views.register, name='register'),
    path('login/', views.LogInUser.as_view(), name='login'),
    path('logout/', views.LogUserOut, name='logout'),
    path('api/questions', views.QuestionListApi.as_view(), name='questionListApi'),
    path('api/question/<int:pk>', views.question_details_api,
         name='questionDetailsApi'),
    path('api/choices', views.Choice_List_Api.as_view(), name='ChoiceListApi'),
    path('api/choice/<int:pk>', views.choice_details_api,
         name='choiceDetailsApi'),
]
"""Using Q Class"""
# path('Q', views.Q.as_view(), name='Q'),
