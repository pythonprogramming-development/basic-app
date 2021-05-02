# To call the view, we need to map it to a URL - and for this we need a URLconf.


from django.urls import path
from polls.views import AboutView
from django.urls import path

from . import views
## to differentiate from other pages url add app_name
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'), # captures” part of the UR <>
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('about/', AboutView.as_view()),
    path('', views.index, name='index'),


]