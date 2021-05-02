from django.shortcuts import render

from django.views.generic.list import ListView 
from .models import GeeksModel 
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView  
  
# Relative import of GeeksForm 
from .forms import GeeksForm 
class GeeksList(ListView): 
  
    # specify the model for list view 
    model = GeeksModel 



class GeeksCreate(CreateView): 
  
    # specify the model for create view 
    model = GeeksModel 
  
    # specify the fields to be displayed 
  
    fields = ['title', 'description'] 

class GeeksUpdateView(UpdateView): 
    # specify the model you want to use 
    model = GeeksModel 
  
    # specify the fields 
    fields = [ 
        "title", 
        "description"
    ] 
  
    # can specify success url 
    # url to redirect after successfully 
    # updating details 
    success_url ="/"

class GeeksDeleteView(DeleteView): 
    # specify the model you want to use 
    model = GeeksModel 
      
    # can specify success url 
    # url to redirect after sucessfully 
    # deleting object 
    success_url ="/"


class GeeksFormView(FormView): 
    # specify the Form you want to use 
    form_class = GeeksForm 
      
    # sepcify name of template 
    template_name = "classbasedApp/templates / geeksmodel_form.html"
  
    # can specify success url 
    # url to redirect after successfully 
    # updating details 
    success_url ="/thanks/"
  
    def form_valid(self, form): 
        # This method is called when valid form data has been POSTed. 
        # It should return an HttpResponse. 
          
        # perform a action here 
        print(form.cleaned_data) 
        return super().form_valid(form) 