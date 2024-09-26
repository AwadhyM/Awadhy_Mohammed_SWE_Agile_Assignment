# Software Engineering & Agile Assignment Application

## Introduction

This Django project is a web application that serves as a Knowledge Management
System for an organisation. The purpose of this application is that an organisations
employees can better share their knowledge through the publication of articles.

Users are required to login to their account in order to access the features of this
application. Once logged in users are free to create, and modify their own articles.
In addition to being able to personalise their account details so that other users can
know more about them.

## How to access the application

The website is currently being hosted through Render. You can access and use the application through the following link.

`(https://awadhy-mohammed-swe-agile.onrender.com/)`


## How to build the application for local use - MacOS & Linux

### Dependencies
>[!IMPORTANT]
>The applications dependencies can be installed from requirements.txt and the guidance for this is set out in the instructions below.
You are however required to have Python already installed so that you can create and enter a virtual environment. In addition to calling pip.

#### Clone the repository source code from Github

```sh
git clone git@github.com:AwadhyM/Awadhy_Mohammed_SWE_Agile_Assignment.git
```

#### 1. Navigate to the directory where the django project is stored
```sh
cd swe_agile_assignment
```

#### 2. Set up your virtual environment
```sh
python3 -m venv venv
```

#### 3. Enter your virtual environment
```sh
source /venv/bin/activate
```

#### 4. Install project dependencies
```sh
pip install -r requirements.txt
```

#### 5. Run the application locally
```
python manage.py runserver
```

The local application is connected to a PostgresSQL database and so any changes made locally
will also be replicated on the hosted version and vice versa.
