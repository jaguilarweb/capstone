# Translation Management Tool App

## Introduction

**Translation Management Tool App** is my FSND final project. 

The core of this application helps to manage translation projects and it has a weighted word count calculator tool in the front-end that brings support to the project managers when managing workloads to translators.

This application follow a REST architectural style and the API returns JSON-encoded responses, and it uses standard HTTP response codes. 


## Accessing the Translation Management Tool App on the web

This application has been deployed in Heroku and it is currently working at this link:

https://fsnd-capstone-jaguilar.herokuapp.com/

In the home page you can login and logout with two different roles.


### Manager: 
Full access, with the ability to get details views, and to list, update, and delete all entities.

```
Manager login credentials
User: manager@example.com
Password: test_manager_2020 
```

```
Token (which can be expired at - "2021-03-19 / 19:09:51 / GMT-03000"):
```

`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVudTVmRzc2NHRYM2RTeTBfU3A1UCJ9.eyJpc3MiOiJodHRwczovL2Rldi1mc25kLTIwMjEudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMDY0ZjNkMTUyMjE4MDA2YTNjYzEwMCIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjE2MTA1MzkxLCJleHAiOjE2MTYxOTE3OTEsImF6cCI6IkZxNjlTbTNMSTFRbDBKb3k4cmpVQ2VobTNlMk1xcHFSIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6cGVyc29uIiwiZGVsZXRlOnByb2plY3QiLCJkZWxldGU6c2VydmljZSIsImdldDpwZXJzb24iLCJnZXQ6cGVyc29uLWRldGFpbCIsImdldDpwcm9qZWN0IiwiZ2V0OnByb2plY3QtZGV0YWlsIiwiZ2V0OnNlcnZpY2UtZGV0YWlsIiwicGF0Y2g6cGVyc29uIiwicGF0Y2g6cHJvamVjdCIsInBhdGNoOnNlcnZpY2UiLCJwb3N0OnBlcnNvbiIsInBvc3Q6cHJvamVjdCIsInBvc3Q6c2VydmljZSJdfQ.Zby-co_aKcajUJLQF6l6ad6y_wkFdPxqDuUq_5wFocf-OFCEG-MmJt9LmNfuAy-rkUPCI9glvJZmAl-Irb4n5ZaK-SEZnfkO-OnCCSnvbtb5HUKf2jC5Ouz5Y0oGVWsmsbl6v4C1EkiF-R7hVGFCw_xFm3K5XKPRkdEckFm0x09ARs7JvL1yOECZHKLdSMnEnVReJY2zHFF_sPZFNhmuMwO7KhthR-51wexz5Di6asDNaZRd-A1E3L0jOmYvEA91adSQC_GhVaGsHWXCyPpd_TMJ3mC4w1hx0RMTGw2Td-047Pu_jT9oOvNeFjbo_gAhdihbLqANaq2nd7_ib6q_3A`

### Project Manager: 
Limited access with the following features:
- Get lists and detail view to all entities;
- Update and create people and project objects;
- Deletion of records is not allowed.

```
Project Manager login credentials
User: pm@example.com
Password: test_pm_1212
```

```
Token (which can be expired at - "2021-03-19 / 19:17:01 / GMT-03000"):
```

`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVudTVmRzc2NHRYM2RTeTBfU3A1UCJ9.eyJpc3MiOiJodHRwczovL2Rldi1mc25kLTIwMjEudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNDE3NDM5MGQ5ZjcxMDA3MGVlMmY3NSIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjE2MTA1ODIxLCJleHAiOjE2MTYxOTIyMjEsImF6cCI6IkZxNjlTbTNMSTFRbDBKb3k4cmpVQ2VobTNlMk1xcHFSIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6cGVyc29uIiwiZ2V0OnBlcnNvbi1kZXRhaWwiLCJnZXQ6cHJvamVjdCIsImdldDpwcm9qZWN0LWRldGFpbCIsImdldDpzZXJ2aWNlLWRldGFpbCIsInBhdGNoOnBlcnNvbiIsInBhdGNoOnByb2plY3QiLCJwb3N0OnBlcnNvbiIsInBvc3Q6cHJvamVjdCJdfQ.Kr23IiwBgKt9B4lr4qBzxl-7V6jhzBCp-AEGk_MO8hGxefzDx3cHplrXLHlpuRmidnS2t68OLztcpbGT6leISA_4ijAXCWUwBvDEHa_lYgHgMN1FXkiHVd9GEDiBYGeWjfo7gQXaLdGAtP-ZD1E720bREZghF4usOzenmov-PDLDaEnbWbbQkQuw_PtbfOZ7RnH2ZQ1c7_t9ZGEieMKQlRCctEyvYj4wNhimExkkTfPQ0JqD_yaObdumJulfuKxnOY-FqCQ10YXjR7Eb5ArXF_Y25vAxfrWw66d0svlPV4pRYibB6HAf4zl7nbbN8RxADiutpKACtMatv5PFzRWVzA`


## Installing Dependencies to run local
#### Python 3.7

Pleasem follow the instructions to install the latest version of Python for your platform from [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

It is recommended to work within virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have completed the virtual environment setup and running, please install the key dependencies:

```bash
pip install -r requirements.txt
```

This command will install all the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight sqlite database. You will primarily work in app.py and may reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


## Running the server

First, please ensure you are working using your created virtual environment.

To run the server, plese execute these commands:

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
    *	This endpoint create a new service, which will require the name, source, and destination.
    *	It returns the success value and service list.
-	Authorization:
    *	Authorization required. 

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
            "name": "Interpretation",
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
    *	It deletes the service of the given ID if it exists. It returns a success value, and all values of the deleted service.

-	Authorization:
    *	Authorization required.

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
    *	This endpoint create a new person, which will require the name, email, rate per word and rate per hour.
    *	It returns the success value and people list.
-	Authorization:
    *	Authorization required. 

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
    *	It delete the person of the given ID if it exists. It returns success value, and all values of the deleted person.

-	Authorization:
    *	Authorization required.

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
    *	This endpoint create a new project, which will require the name, kind, deadline, person id and service id.
    *	It returns the success value and projects list.
-	Authorization:
    *	Authorization required. 

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
    *	It deletes the project of the given ID if it exists. It returns success value, and all values of the deleted project.

-	Authorization:
    *	Authorization required.

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

The API will return the these error types when the requests fails:
-	400: Bad Request
-	404: Resource Not found
-	405: Method not allowed
-	422: Unprocessable
-	500: Internal Server Error



## Testing
To run the tests, you should create an alternative database. In this case capstone_test.
```
dropdb capstone_test
createdb capstone_test
python test_app.py
```

## Authors

These application and documentation were created by Jenny Aguilar.
