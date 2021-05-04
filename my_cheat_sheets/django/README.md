
### Starting up

#### Virtual enviorement
Task  |  Command
--|--
Create a virtual enviorement |  `python3 -m venv <folder_name_to_locate_the_venv> `
Activate the venv (Linux & Mac)  | `source <folder_name_to_locate_the_venv>/bin/activate`
Activate the venv (Linux & Mac)   |  `deactivate`


#### First project

Task  |  Command
--|--
Creating a project | `django-admin startproject mysite`
Creating an app  |  `python manage.py startapp myapp`
Make migrations (let django write SQL instructions for you )  |  `python manage.py makemigrations`
Make migrations for a specific app  | `python manage.py makemigrations myapp`
Apply those migrations to the db  |  `python manage.py migrate`
Run dev server  |  `python manage.py runserver`
Run dev server specificing port |  `python manage.py runserver <port>`
Run dev server in your local network |  `python manage.py runserver <your_local_ip_address>:<port>`



## Being productive
Task  |  Command
--|--
Save venv packages in file | `pip freeze > requirements.txt`
Install from requirements  |  `pip install -r requirements.txt`



## Understanding the settings
Task  |  Command
--|--
BASE_DIR  |  is where your *manage.py* lies
PROJECT_ROOT  |  is BASE_DIR + your_project_name (where *settings.py* is)


## More

### [Register and customize your models in the admin area](myapp/admin.md)
