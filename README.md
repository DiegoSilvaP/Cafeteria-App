# Cafeteria-App
This is a django application made for the *"Welcome to django"* workshop

This is the list of the packages you need and installations commands

+ Django (*Python web framework*) `python -m pip install django==3.0.1`
+ Pillow (*To have "ImageField" as models property to save images*) `python -m pip install Pillow`
+ Baton (*Admin panel theme*) `python -m pip install django-baton`
+ Ck editor (*Advanced text editor such as Microsoft Word*, this is used in the *Information* app) `python-m pip install django-ckeditor`

---

## Remember you must create a virtual environment to install this version of the packages and they don't interfere with other versions

## This is the cheat sheet of the most used commands in the django world.

+ `python -m pip install PackageName==version` This is used to install a package in a python environment, where *==version* parameter is __optional__, if you don't specify it, pip will install the newest package version
+ `virtualenv name` This is used to create a virtual environment, where *name* specifies the name of the virtual environment


To activate the virtual environment (windows command), run `name\Scripts\activate` where *name* specifies the name of the virtual environment.
You can ensure that your virtual environment is enabled in your command window if the promp shows __(*name*)__ where *name* specifies the name of the virtual environment, e.g. 


`c:\> virtualenv django3`
`c:\> django3\Scripts\activate`
__`(django3)`__`c:\>`
+ `django-admin startproject name` This is used to create a new django project, where *name* specifies the name of the project
+ `python manage.py startapp name` This is used to create a new app inside the django project, where *name* specifies the name of the app
+ `python manage.py createsuperuser` This is used to create a super user which has acces to all permissions of the admin panel
+ `python manage.py makemigrations appname` This prepares all the changes made on the models of the project, where *appname* is represents the name of the app you want to create migrations, and it's totally __optional__, you have to specified when django says __No changes__ but you know you have pendient changes to migrate
+ `python manage.py migrate` This is used to reflect all the chages made on models of the project to the database, and this is possible because before you had to run the `makemigrations` command
`python manage.py runserver portnumber` This is used to run your server locally, so you can see your website, where *portnumber* is totally __optional__ and specifies the port of the server, this is useful when you have multiple django projects running on the same computer but in different ports