# Introduction
The project is created by Devesh Kumar and Piyush Garg while participating in Flipr Hackathon 6.0.
cov19stats is a scalable Django-based web application that displays the live statistics of COVID-19 virus cases, emergency contacts and advisories from Government of India.

# Installation
After cloning the project, follow these steps to download and run the

   
    $ virtualenv venv
    $ source ./venv/bin/activate
    $ cd cov19stats
    $ pip install -r requirements
    $ python manage.py migrate
    $ python manage.py runserver

After that visit http://127.0.0.1:8000/
