"""testSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include 
from testSite.views import basic_view, hello_geek, geeks_view
from basicGuide.views import home_view
from polls.views import home_view
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    #  path('', include("projectApp.urls")), 
    #  path('', include("classbasedApp.urls")), 
    path('', home_view), 

    path('geek/', geeks_view), 
    # path('', hello_geek),
    ## add pages route
    # point the root URLconf at the polls.urls module. In mysite/urls.py,

    path('polls/', include('polls.urls')), ## you can also first empty string in first parameter 
    path('home/', home_view), ## you can import method from any page directly and show the response
    
    path('', basic_view), ## you can import method from any page directly and show the response
]


