# HttpResponse is used to pass the information back to view 

## it is optional file if you want to add views here in main page then you can add that


from django.http import HttpResponse 
import datetime 
# Defining a function which will receive request and perform task depending upon function definition 
def hello_geek (request) : 
  
    # This will return Hello Geeks 
    # string as HttpResponse 
    return HttpResponse("Hello Geeks")


  
# create a function 
def geeks_view(request): 
    # fetch date and time 
    now = datetime.datetime.now() 
    # convert to string 
    html = "Time is {}".format(now) 
    # return response 
    return HttpResponse(html)  

# Defining a function which  will receive request and  perform task depending  upon function definition 

def basic_view(request): 
    # fetch date and time 
    now = datetime.datetime.now() 
    # convert to string 
    html = "Time is {}".format(now) 
    # return string as HttpResponse 
    return HttpResponse(html)  

