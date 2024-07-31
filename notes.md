- Starting a new project:
    - What is it?
        python -m pip install pip setuptools wheel --upgrade

- Create a project
    - django-admin startproject projet-name .

- Executing django commands
    - django-admin
    <br>OR 
    - python manage.py 'python manage.py' in most cases

- Static files
    - Static and "Global Static"
    - STATIC_URL = ""
    - STATICFILES_DIR = []
    - Command to collect all static files → collectstatic
        - settings.py: STATIC_ROOT → folder name to collect static files