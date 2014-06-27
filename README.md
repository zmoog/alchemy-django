# Alchemy

## Quickstart

This quickstart describe the project setup on a Unix-like OS. It has been tested on OS X Mavericks. 

Install virtualenv if it's not already there:

```bash
$ sudo easy_install virtualenv
```

Create a directory to host the project files:

```bash

$ mkdir -p ~/code/projects/your-nickname/alchemy-django

$ cd ~/code/projects/your-nickname/alchemy-django

$ git clone https://github.com/zmoog/alchemy-django.git

```

Prepare and activate a new virtual environment for the project:

```bash

$ mkdir -p ~/code/envs/

$ cd ~/code/envs/

$ virtualenv alchemy-django

$ echo 'export DJANGO_SECRET_KEY="some secret here"' >> ~/code/envs/alchemy-django/bin/activate

$ source ~/code/envs/alchemy-django/bin/activate
```

Install required Python packages:

```bash

$ cd ~/code/projects/your-nickname/alchemy-django

$ pip install -r requirements/local.txt

```

Prepare the database and authentication:

```bash
$ python manage.py syncdb --settings=alchemy.settings.local

```


And finally run the server:

```bash

$ python manage.py runserver --settings=alchemy.settings.local
Validating models...

0 errors found
June 27, 2014 - 04:05:08
Django version 1.6.5, using settings 'alchemy.settings.local'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```
