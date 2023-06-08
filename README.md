# Uri's Diner

A full stack Django web app that simulates a restaurant's takeout website. Check out the [live website](https://uris-diner-site.wittywave-70237434.germanywestcentral.azurecontainerapps.io/) or [run locally](#running-locally).

## Features:
- Creating a user
- Viewing the menu and adding dishes to your cart
- Reviewing your cart and placing an order
- Viewing your active and past orders
- Restaurant's manager back office, with ability to change the menu and fulfill orders

## Frameworks and capabilities:
- Backend, templating and models built purely with Django
- PostgreSQL database on Azure (SQLite on local version)
- Images are uploaded using [Azure storage](https://django-storages.readthedocs.io/en/latest/backends/azure.html) (on local version, images are saved to `/media` ). Image processing capabilities provided by [Pillow](https://pypi.org/project/Pillow/)
- Designed using [Materialize CSS](https://materializecss.com) and customized with Sass
- Fully responsive design:

<img src="https://raw.githubusercontent.com/ugthefluffster/uris_diner/main/example-images/menu-tablet.png" height="250">
<img src="https://raw.githubusercontent.com/ugthefluffster/uris_diner/main/example-images/menu-phone.png" height="250">

  ---
## Running locally (Windows):
Install [python](https://www.python.org/downloads/) and clone repository, then install requirements:  
`pip install -r requirements.txt`  

Switch to local-db-version branch:  
`git checkout local-db-version`

Run the server:  
`py manage.py runserver`
