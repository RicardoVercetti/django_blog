# Notes

## start-up

- `sudo apt install python3.10-venv` for installing venv in debian/ubuntu based systems
- `python3 -m venv blogenv` for creating the virtual env
- `source blogenv/bin/activate` for activating the env
- `pip install django` for installing django(install inside the env)
- `django-admin --version` to check if its installed
- `django-admin startproject myblog` to create a new django project
- `python manage.py runserver` to run the development server(have to `cd myblog` before)
- `python manage.py startapp blog` Create a Blog App
- create models(at models.py) and make migrations `python manage.py makemigrations` and `python manage.py migrate`
- `python manage.py createsuperuser` create super admin (and register your model in blog/admin.py)

### Don't forget these

- Django looks for registration inside templates/registration/...


### what to do
 - sign up should check if the username already exists
 - logging in should lead to home page of the logged in user
 - no pages should be accessible if not logged in
 - posts should have author names
 - what about the 

### Users 
 - pineforest 	pinecake
 - tim 			timtaller
