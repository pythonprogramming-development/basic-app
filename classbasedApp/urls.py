from django.urls import path 
  
# importing views from views..py 
from .views import GeeksList, GeeksCreate , GeeksUpdateView, GeeksDeleteView
urlpatterns = [ 
    path('', GeeksList.as_view(template_name="geeksmodel_list.html")), 
    # path('form', GeeksFormView.as_view()), 
     path('create', GeeksCreate.as_view(template_name ="geeksmodel_form.html") ),
         # <pk> is identification for id field,  
    # <slug> can also be used  
    path('<pk>/update', GeeksUpdateView.as_view(template_name ="geeksmodel_form.html")),
    path('<pk>/delete/', GeeksDeleteView.as_view(template_name = "geeksmodel_confirm_delete.html")) 
] 

   
