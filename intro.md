Django framework basic setup

Introduction-

It is fully featured server-side web application framework.

In this, web pages and other content are delivered by views.

Page’s design is hard-coded in the view. The view can read records from a database.

All this wants is that HttpResponse.

views-

Its views are divided into two major categories:-

Function-Based Views- implemented with logics for creating, update, retrieve and delete views.

Class-Based Views

pip(python package manager)-

pip is used to install python packages.

>pip3 list

>flask –version
>pip list

To install a particular package-

>pip3 install django~=2.2 or python -m pip install [packagename] or py -m pip install [packagename]
>python -m pip install Pillow

To install python project packages-

>pip install -r requirements.txt

To check all project packages-

>pip3 freeze

>pip freeze

To get information on any package visit this site.

To check the python version-

>py -3 -V

To check version-

>py -3 -m django --version

To create a new project-

django-admin startproject projectName - create new project

To change directory-

cd projectname

To run the project-

Python manage.py runserver

It will run your project on http://127.0.0.1:8000/

To run the app on a different port-

python manage.py runserver 8081

What 127.0.0.1 means?

If you call the IP Address 127.0.0.1 then you are communicating with the localhost your own computer

To create a new page-

python manage.py startapp projectApp
python manage.py startapp polls

projectApp and polls are page names.

To create superuser-

Before creating a superuser you must need to migrate your changes. This superuser is needed when you are saving data to the database.

>python manage.py migrate

To create admin login-

>python manage.py createsuperuser

After this, you can create a username and password.

To create a Database-
After creating models, you need to migrate those changes-

python manage.py makemigrations
python manage.py makemigrations polls # for particular page
python manage.py migrate

File structure-

manage.py- to create one or more applications

settings.py- registering any applications we create, the location of our static files, database configuration details

urls.py- defines the site URL-to-view mappings.

wsgi.py- communicate with the webserver

It supports 5 main databases PostgreSQL, MariaDB, MySQL, Oracle, and SQLite.

By default, the configuration uses SQLite.

In future real projects scalable database like PostgreSQL.

it supports all the common database relationships: many-to-one, many-to-many, and one-to-one

To include the app in our project, you need to add a reference to its configuration class in the INSTALLED_APPS setting.

suppose you created a page polls. It will create some files to write the page logic. By default, it includes URLs, apps.py files etc. To create the path check the the PollsConfig class is in the polls/apps.py file, So its dotted path is 'polls.apps.PollsConfig'

Update the mysite/settings.py file add it to INSTALLED_APPS. Here mysite is a master page means main application page.

To Make the poll app modifiable in the admin

Register this in the polls/admin.py file.

from .models import Question

admin.site.register(Question)

Django’s Template system

Using angle brackets “captures” part of the URL .

create a directory called templates in your polls directory

All POST forms that are targeted at internal URLs should use the {% csrf_token %} template tag.

To setup virtual environment-

>py -m pip install virtualenvwrapper-win
py -m venv my_django_environment
mkvirtualenv my_django_environment
.\new_env\Scripts\activate

py -m pip install Django

Windows

cmd.exe

> my_django_environment\Scripts\activate

To clear the database run the below command it will clear data from this

http://127.0.0.1:8000/admin

python manage.py flush

It also clears your admin username and password. After this, you have to create other credentials.

Common Errors solution-

move locals.py in the setting of the main default page.

nodejs/django architecture
multiple request processing
hello world
controller
services
middleware
concurrency

eduonix
django : http://bit.ly/2F7rG1r
Coupon code: NIFREE

http://www.djangoproject.com/