# Restaurant API
It’s a restaurant API where you can create, update and delete a restaurant (identified by its name), and also list restaurants,
get a restaurant by name and get a random restaurant.

- Default DB SQLite3
- Restaurants names are unique

# Installation
1. Clone the project
2. Create virtual environment for python version == 3.9
```virtualenv venv -p python 3.9```
3. Copy and fill in example_restaurant.conf, rename it
as restaurant.conf. If you store this file not in the root
directory, add an environment variable:
```CONFIG_PATH=/path/to/config_file.conf```
4. Install python requirements
```pip install -r REQUIREMENTS.txt```
5. Migrate django migrations
```python manage.py migrate```
6. Run the project
```python manage.py runserver```