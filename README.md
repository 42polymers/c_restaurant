# Restaurant API
It’s a restaurant API where you can create, update and delete a restaurant (identified by its name), and also list restaurants,
get a restaurant by name and get a random restaurant.

- Default DB SQLite3
- Restaurants names are unique

# Simple installation
1. Clone the project
2. Select the root directory
```cd c_restaurant```
3. Create virtual environment for python version == 3.9
```virtualenv venv -p python 3.9```
4. Change the working environment
```source venv/bin/activate```
5. Copy and fill in example_restaurant.conf, rename it
as restaurant.conf. If you store this file not in the root
directory, add an environment variable:
```CONFIG_PATH=/path/to/config_file.conf```
6. Install python requirements
```pip install -r REQUIREMENTS.txt```
7. Migrate django migrations
```python restaurant/manage.py migrate```
8. Run the project
```python restaurant/manage.py runserver```

# Installation with Docker
1. Ensure you have running Docker
2. Clone the project
3. Select the root directory
```cd c_restaurant```
4. Copy and fill in example_restaurant.conf, rename it
as restaurant.conf
5. Build an image
```docker build . -t image_name```
6. Run docker-compose
```docker-compose up```
