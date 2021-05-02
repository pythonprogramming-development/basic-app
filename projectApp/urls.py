
from django.urls import path
from testSite.views import hello_geek
from projectApp.views import list_view
from projectApp.views import create_view

from .views import detail_view, update_view, delete_view
  

urlpatterns = [
#     path('', list_view), 
#     path('create', create_view), 
# path('<id>', detail_view ), 
#     path('hii', hello_geek), 
#     path('<id>/update', update_view ),
# path('<id>/delete', delete_view ),

]