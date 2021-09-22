# Restaurant API
It’s a restaurant API where you can create, update and delete a restaurant (identified by its name), and also list restaurants,
get a restaurant by name and get a random restaurant.

- Default DB SQLite3
- Restaurants names are unique

# Installation
1. Clone the project
2. Select the root directory:
```cd c_restaurant```
3. Create virtual environment for python version == 3.9:
```virtualenv venv -p python 3.9```
4. Change the working environment:
```source venv/bin/activate```
5. Copy and fill in example_restaurant.conf, rename it
as restaurant.conf. If you store this file not in the root
directory, add an environment variable:
```CONFIG_PATH=/path/to/config_file.conf```
6. Install python requirements:
```pip install -r REQUIREMENTS.txt```
7. Migrate django migrations:
```python restaurant/manage.py migrate```
8. Run the project:
```python restaurant/manage.py runserver```
9. The application is running at the 8000 port

# Deploying with Docker
1. Ensure you have a running Docker
2. Clone the project
3. Select the root directory:
```cd c_restaurant```
4. Copy and fill in "example_restaurant.conf", rename it
as "restaurant.conf"
5. Build an image:
```docker build . -t image_name```
6. Run docker-compose:
```docker-compose up```
7. The application is running at the 8001 port

# Tests
There are several tests for the restaurant API.
Command to run the tests:
```python /path/to/manage.py test```
The tests are running automatically during the Docker application composing

# Examples
- get the project schema:
```GET /```
- get the list of restaurants:
```GET /restaurants``` 
- create a restaurant:
```POST /restaurants with {"name":<restaurant_name>} in JSON data```
- get a restaurant:
```GET /restaurants/<restaurant_name>```
- update a restaurant:
```PUT /restaurants/<restaurant_name> with {"name":<restaurant_new_name>} in JSON data```
- delete a restaurant:
```DELETE /restaurants/<restaurant_name>```
- get a random restaurant:
```GET /restaurants_random```
