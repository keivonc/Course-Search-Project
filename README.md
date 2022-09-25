# Creating and activating the virtual environment
First step is to create and activtae your virtual environment. If you've already done this, skip this step. 
1. Install [virtualenv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
2. Create your virtual env by running `py -m venv env` (Windows) or `python3 -m venv env` (Mac/Unix) in your terminal from the project directory (should be project-a-29). You can make the "env" part "venv" if you would like, but it should be one of the two.
3. Activate you virtual environment. I do this by running `./env/Scripts/activate` (casing matters)

In your terminal, you should see `(env) PS C:\...` if you're using Windows Powershell. If you're using Mac you should see something similar. Make sure whenever you run any part of the app that you are in this environment.

# Installing dependencies

There are a few commands to be familiar with regarding the dependencies. Make sure that you have your virtual environment activated when you run these.

### Installing Existing Requirements

`pip install -r requirements.txt`

### Updating the project requirements

`pip freeze > requirements.txt`
You would do this if you installed a new project dependency. For example, if I needed to install django-bootstrap5, I would run `pip install django-bootstrap5` then the command above.

### Viewing Existing Packages in the Current Environment

`pip list`
