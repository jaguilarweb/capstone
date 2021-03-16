# Translation Management Tool App

## Introduction

**Translation Management Tool App** is my FSND final project. 

The core of this aplication helps to manage translation projects and has a ponderate word count calculator tool in the front-end that support to the project managers to manage assign workloads to translators.

This application conforms to the REST architectural style, and the API returns JSON-encoded responses and uses standard HTTP response codes. 

You can use too their front-end interface that allow to access a feature that calculate automatically the total of project on depend the individual rates and word counts ponderated.


## Accessing the Translation Management Tool App on the web

This aplication has been deployed to Heroku and is currently working at this link:

http: 

In the home page you can login and logout with two differents roles.


### Manager: 
Full access, with the ability to get details views, list, update, and delete all entities.
```
Manager login credentials
User: manager@example.com
Password: test_manager_2020 
```

### Project Manager: 
Limit access, with the ability to:
- Get lists and details view to all entities
- Update and Create people and projects
- Delete records is not allowed
```
Project Manager login credentials
User: pm@example.com
Password: test_pm_1212
```

## Installing Dependencies to run local
#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


## Running the server

First ensure you are working using your created virtual environment.

To run the server, execute:

```bash
source setup.sh
flask run
```

## API Reference

### GET '/services'

-	General:
    *	This endpoint should return a list of services.

-	Authorization:
    *	Not authorization required. 

-	Sample: curl http://127.0.0.1:5000/services
```
{
    "services": [
        {
            "destiny": "RS",
            "id": 1,
            "name": "DTP",
            "source": "EN"
        },
        {
            "destiny": "Spanish",
            "id": 2,
            "name": "Interpratation",
            "source": "English"
        }
    ],
    "success": true
}
```

### GET Detail '/services/{service_id}'

-	General:
    *	This endpoint should return a detail view of service by id.

-	Authorization:
    *	Authorization required. 

-	Sample: curl -H "Authorization: Bearer **ADD_TOKEN**"  http://127.0.0.1:5000/api/services/2
```
{
    "service": {
        "destiny": "Spanish",
        "id": 2,
        "name": "Interpratation",
        "source": "English"
    },
    "success": true
}
```


### POST '/services'

-	General:
    *	This endpoint create new service, which will require the name, source, and destiny.
    *	Returns the success value and services list.
-	Authorization:
    *	Authorization requiered. 

- Sample: curl -X POST -H "Authorization: Bearer **ADD_TOKEN**" -H "Content-Type: application/json" -d '{"name":"Translation", "source":"English", "destiny":"Spanish"}' http://127.0.0.1:5000/api/services

```
{
    "services": [
        {
            "destiny": "RS",
            "id": 1,
            "name": "DTP",
            "source": "EN"
        },
        {
            "destiny": "Spanish",
            "id": 2,
            "name": "Interpratation",
            "source": "English"
        },
        {
            "destiny": "Spanish",
            "id": 4,
            "name": "Translation",
            "source": "English"
        }
    ],
    "success": true
}
```

### DELETE '/services/{service_id}'

-	General:
    *	Deletes the service of the given ID if it exists. Returns success value, and all values of the deleted service.

-	Authorization:
    *	Authorization requiered.

-	Sample: curl -X DELETE -H "Authorization: Bearer **ADD_TOKEN**"  http://127.0.0.1:5000/api/services/4

```
{
    "services": {
        "destiny": "Spanish",
        "id": 4,
        "name": "Translation",
        "source": "English"
    },
    "success": true
}

```

### GET '/people'

-	General:
    *	This endpoint should return a list of people.

-	Authorization:
    *	Authorization required. 

-	Sample: curl -H "Authorization: Bearer **ADD_TOKEN**" http://127.0.0.1:5000/people
```
{
    "people": [
        {
            "email": "carlos@example.com",
            "id": 2,
            "kind": "Externo",
            "name": "Carlos Lopez",
            "rateh": 15.0,
            "ratew": 0.02
        },
        {
            "email": "alexs@prueba.com",
            "id": 3,
            "kind": "Freelance",
            "name": "Alexander fuentes",
            "rateh": 3.0,
            "ratew": 0.2
        }
    ],
    "success": true
}
```

### GET Detail '/people/{person_id}'

-	General:
    *	This endpoint should return a detail view of person by id.

-	Authorization:
    *	Authorization required. 

-	Sample: curl -H "Authorization: Bearer **ADD_TOKEN**"  http://127.0.0.1:5000/api/people/2
```
{
    "person": {
        "email": "carlos@example.com",
        "id": 2,
        "kind": "Externo",
        "name": "Carlos Lopez",
        "rateh": 15.0,
        "ratew": 0.02
    },
    "success": true
}
```


### POST '/people'

-	General:
    *	This endpoint create new person, which will require the name, email, rate per word and rate per hour.
    *	Returns the success value and people list.
-	Authorization:
    *	Authorization requiered. 

- Sample: curl -X POST -H "Authorization: Bearer **ADD_TOKEN**" -H "Content-Type: application/json" -d '{"name":"Alexander Fuentes", "kind":"Freelance", "email":"alexs@prueba.com", "ratew":0.2, "rateh":3.0}' http://127.0.0.1:5000/api/people

```
{
    "people": [
        {
            "email": "carlos@example.com",
            "id": 2,
            "kind": "Externo",
            "name": "Carlos Lopez",
            "rateh": 15.0,
            "ratew": 0.02
        },
        {
            "email": "alexs@prueba.com",
            "id": 3,
            "kind": "Freelance",
            "name": "Alexander Fuentes",
            "rateh": 3.0,
            "ratew": 0.2
        }
    ],
    "success": true
}
```

### DELETE '/people/{person_id}'

-	General:
    *	Deletes the person of the given ID if it exists. Returns success value, and all values of the deleted person.

-	Authorization:
    *	Authorization requiered.

-	Sample: curl -X DELETE -H "Authorization: Bearer **ADD_TOKEN**"  http://127.0.0.1:5000/api/people/1

```
{
    "person": {
        "email": "carlos@example.com",
        "id": 1,
        "kind": "Externo",
        "name": "Carlos Lopez",
        "rateh": 2.0,
        "ratew": 0.01
    },
    "success": true
}

```

### GET '/projects'

-	General:
    *	This endpoint should return a list of projects.

-	Authorization:
    *	Authorization required.

-	Sample: curl -H "Authorization: Bearer **ADD_TOKEN**" http://127.0.0.1:5000/projects
```
{
    "projects": [
        {
            "deadline": "Mon, 05 Apr 2021 00:00:00 GMT",
            "hour_count": 0.0,
            "id": 1,
            "kind": "Project",
            "name": "Pro_032021",
            "person_id": 2,
            "rate": 0.0,
            "service_id": 2,
            "word_count": 0
        },
        {
            "deadline": "Sun, 25 Apr 2021 22:00:00 GMT",
            "hour_count": 0.0,
            "id": 3,
            "kind": "Asign",
            "name": "888-HGYD-R",
            "person_id": 2,
            "rate": 0.0,
            "service_id": 1,
            "word_count": 0
        }
    ],
    "success": true
}
```

### GET Detail '/projects/{project_id}'

-	General:
    *	This endpoint should return a detail view of project by id.

-	Authorization:
    *	Authorization required. 

-	Sample: curl -H "Authorization: Bearer **ADD_TOKEN**"  http://127.0.0.1:5000/api/projects/1
```
{
    "project": {
        "deadline": "Sun, 25 Apr 2021 22:00:00 GMT",
        "hour_count": 0.0,
        "id": 3,
        "kind": "Asign",
        "name": "888-HGYD-R",
        "person_id": 2,
        "rate": 0.0,
        "service_id": 1,
        "word_count": 0
    },
    "success": true
}
```

### POST '/projects'

-	General:
    *	This endpoint create new project, which will require the name, kind, deadline, person id and service id.
    *	Returns the success value and projects list.
-	Authorization:
    *	Authorization requiered. 

- Sample: curl -X POST -H "Authorization: Bearer **ADD_TOKEN**" -H "Content-Type: application/json" -d '{"name":"Pro_032021", "kind":"Project", "deadline":"2021-04-05", "person_id":2, "service_id":2}' http://127.0.0.1:5000/api/projects

```
{
    "projects": [
        {
            "deadline": "Mon, 05 Apr 2021 00:00:00 GMT",
            "hour_count": 0.0,
            "id": 1,
            "kind": "Project",
            "name": "Pro_032021",
            "person_id": 2,
            "rate": 0.0,
            "service_id": 2,
            "word_count": 0
        },
        {
            "deadline": "Sun, 25 Apr 2021 22:00:00 GMT",
            "hour_count": 0.0,
            "id": 3,
            "kind": "Asign",
            "name": "888-HGYD-R",
            "person_id": 2,
            "rate": 0.0,
            "service_id": 1,
            "word_count": 0
        }
    ],
    "success": true
}
```

### DELETE '/projects/{project_id}'

-	General:
    *	Deletes the project of the given ID if it exists. Returns success value, and all values of the deleted project.

-	Authorization:
    *	Authorization requiered.

-	Sample: curl -X DELETE -H "Authorization: Bearer **ADD_TOKEN**"  http://127.0.0.1:5000/api/projects/2

```
{
    "projects":
    {
        "deadline":"Mon, 05 Apr 2021 00:00:00 GMT",
        "hour_count":0.0,
        "id":1,
        "kind":"Project",
        "name":"Pro_032021",
        "person_id":2,
        "rate":0.0,
        "service_id":2,
        "word_count":0
    },
    "success":true
}

```

### Error Handling

Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "Bad request"
}
```

The API will return three error types when requests fail:
-	400: Bad Request
-	404: Resource Not found
-	405: Method not allowed
-	422: Unprocessable
-	500: Internal Server Error



## Testing
To run the tests, create an alternative database. In this case capstone_test.
```
dropdb capstone_test
createdb capstone_test
python test_app.py
```

## Authors

This aplication and documentation were created by Jenny Aguilar.
