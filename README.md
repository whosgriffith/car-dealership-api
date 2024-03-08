# car-dealership-api

## Installation
For the installation you could use PIPENV or pypi, use the requiremets.txt or pipfile.lock to install the required packages with the correct versions.

```
pipenv install
```
or
```
pip install -r requirements.txt
```

Then for testing purposes you can run the application as any django project:
```
python manage.py makemigrations
```

```
python manage.py migrate
```

```
python manage.py runserver
```

The database used is SQLite for simplicity, can be changed in `settings.py`

For production run on a WSGI server like Gunicorn and serve the media and statics files with NGINX, Whitenoise or some CDN.

## Authorization
PUT, POST and DELETE methods requires authorization, for this send a `Authorization` header with the token of an admin user

Example:

`Authorzation: Token f5d23a3d0bd8ed1a69cc8d1fa9a4ed4ce0469a28`


## Filtering and order
The car list can be filtered and ordered with the following query params:
| Query param | Values           |
| ----------- | -------------- |
| type         | *integer (use the guide with types from below)*  |
| ordering     | `model_year` or `price` |

ID's of type for type filter
 ID | Name                  |
| -- | --------------------- |
| 0  | Autos                 |
| 1  | Pickups y Comerciales |
| 2  | SUVs y Crossovers     |


## Endpoints
Note: You can interact with these endpoints trough SwaggerUI in `/documentation`

#### Documentation
| HTTP Method | Path           | Description                              |
| ----------- | -------------- | ---------------------------------------- |
| GET         | /documentation/ | Serve OpenAPI schema on SwaggerUI |


#### Authentication
| HTTP Method | Path           | Description     |
| ----------- | -------------- | --------------- |
| POST        | /users/signup/ | Create new user |
| POST        | /users/login/   | Get login token |


#### Users
| HTTP Method | Path         | Description          |
| ----------- | ------------ | -------------------- |
| GET         | /users/{id}/ | Retrieve single user |
| DELETE      | /users/{id}/ | Delete user          |


#### Cars
| HTTP Method | Path        | Description         |
| ----------- | ----------- | ------------------- |
| GET         | /cars/      | List of cars        |
| GET         | /cars/{id}/ | Retrieve single car |
| POST        | /cars/      | Create car          |
| PUT         | /cars/{id}/ | Update car          |
| DELETE      | /cars/{id}/ | Delete car          |


#### Car features
| HTTP Method | Path                 | Description                 |
| ----------- | -------------------- | --------------------------- |
| GET         | /cars/features/      | List of car features        |
| GET         | /cars/features/{id}/ | Retrieve single car feature |
| POST        | /cars/features/      | Create car feature          |
| PUT         | /cars/features/{id}/ | Update car feature          |
| DELETE      | /cars/features/{id}/ | Delete car feature          |


#### Car images
| HTTP Method | Path               | Description               |
| ----------- | ------------------ | ------------------------- |
| GET         | /cars/images/      | List of car image         |
| GET         | /cars/images/{id}/ | Retrieve single car image |
| POST        | /cars/images/      | Create car image          |
| PUT         | /cars/images/{id}/ | Update car image          |
| DELETE      | /cars/images/{id}/ | Delete car image          |
