from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    #using angle brackets(<>) captures that part of the URL and sends it as a keyword argument to its view function
    # example, /polls/
    path('', views.IndexView.as_view(), name='index'),
    # example /polls/5
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), 
    # example /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # example /polls/5/votes
    path('<int:question_id>/votes/', views.vote, name='vote')

]