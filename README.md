# Social-login-with-django-allauth
User Authentication with a Google &amp; Facebook Account using Django Allauth

Follow these steps to download and run the
django-allauth example application in this directory:

::
    
    $ mkdir social-login
    $ cd social-login/
    $ git clone https://github.com/emilgeorgejames1/Social-login-with-django-allauth.git
    $ virtualenv venv
    $ . venv/bin/activate
    $ pip install -r requirements.txt

Create the database tables and an admin user.
Run the following and when prompted to create a superuser choose yes and
follow the instructions:

::

    $ python manage.py migrate
    $ python manage.py createsuperuser
    
Setup SSL on local django server.

::

    $ python manage.py runserver_plus --cert certname  
    
It will generate a (self-signed) certificate automatically
    
    
Run the Django development server:

::

    $ python manage.py runserver

Create a Social Application for Google and facebook at http://127.0.0.1:8000/admin/socialaccount/socialapp.

Finally:
 
 login : https://localhost:8000/accounts/login <br />
 signup : https://localhost:8000/accounts/signup <br />
 logout : https://localhost:8000/accounts/logout <br />
 
Reference for Facebook and google app configuration:
  
  http://www.marinamele.com/user-authentication-with-google-using-django-allauth
  
