import os
from flask import Flask, request, abort, render_template, jsonify
from models import *
from flask_bootstrap import Bootstrap
from flask_cors import CORS


#---------------------------------------------------
# App Config
#---------------------------------------------------


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    setup_db(app)
    CORS(app)
    
    return app

app = create_app()

#----------------------------------------------------
# Headers
#----------------------------------------------------

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-type, Authorization')
    response.headers.add('Access-Control_Allow-Methods', 'GET, PATCH, POST, DELETE, OPTIONS')
    return response

#----------------------------------------------------
# Endpoints
#----------------------------------------------------

@app.route('/')
def index():
    gretting = "Hello Word"
    return render_template('pages/home.html', gretting=gretting)

#----------------------------------------------------
# Handler GET request projects
#----------------------------------------------------


@app.route('/projects', methods=['GET'])
@app.route('/api/projects', methods=['GET'])
def get_projects():
    error = False
    project_list = []
    try:
        selection = Project.query.all()
    except:
        error = True
    if error:
        abort(404)
    else:        
        if request.path == '/api/projects':
            project_list = [project.format() for project in selection]
            return jsonify({
                'success': True,
                'projects': project_list
            }), 200
            
        return render_template('pages/projects.html', projects=selection)

#----------------------------------------------------
# Handler POST request project
#----------------------------------------------------


@app.route('/projects', methods=['POST'])
@app.route('/api/projects', methods=['POST'])
def create_project():

    project = {}
    try:
        body = request.get_json()
        name = body.get('name', None)
        kind = body.get('kind', None)
        deadline = body.get('deadline', None)
        word_count = body.get('word_count', None)
        hour_count = body.get('hour_count', None)
        rate = body.get('rate', None)
        person_id = body.get('person_id', None)
        service_id = body.get('service_id', None)
        
        new_project = Project(name=name, kind=kind, deadline=deadline, word_count=word_count, hour_count=hour_count, rate=rate, person_id=person_id, service_id=service_id)
        new_project.insert()
        project = Project.query.filter(Project.id == new_project.id).one_or_none()
        
    except:
        abort(404)
     
    finally:
        new_project.close()
        if request.path == '/api/projects':

            return jsonify({
                'success': True,
                'projects': project.format()
            }), 200

    return render_template('pages/projects.html', projects=project)

#----------------------------------------------------
# Handler PATCH request project
#----------------------------------------------------

@app.route('/projects/<int:project_id>', methods=['PATCH'])
@app.route('/api/projects/<int:project_id>', methods=['PATCH'])
def update_project(project_id):

    project = {}
    try:
        body = request.get_json()
        deadline = body.get('deadline', None)
        word_count = body.get('word_count', None)
        hour_count = body.get('hour_count', None)
        rate = body.get('rate', None)

        up_project = Project.query.filter(Project.id == project_id).one_or_none()
        up_project.deadline = deadline
        up_project.word_count = word_count
        up_project.hour_count = hour_count
        up_project.rate = rate
        up_project.update()
        project = up_project.format()

    except:
        abort(401)
     
    finally:
        up_project.close()
        if request.path == '/api/projects/' + str(project_id):

            return jsonify({
                'success': True,
                'project': project
            }), 200

    return render_template('pages/projects.html', projects=project)

#----------------------------------------------------
# Handler DELETE request project
#----------------------------------------------------

@app.route('/projects/<int:project_id>', methods=['DELETE'])
@app.route('/api/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project= {}
    try:
        
        project_search = Project.query.filter(Project.id == project_id).one_or_none()
        project = project_search.format()
        project_search.delete() 
        
    except Exception as e:
        print(e)
        pass
    
    # except:
    #     abort(401)
     
    finally:
        project_search.close()
        if request.path == '/api/projects/' + str(project_id):

            return jsonify({
                'success': True,
                'projects': project
            }), 200

    return render_template('pages/projects.html', projects=project)    



#----------------------------------------------------
# Handler GET request service
#----------------------------------------------------


@app.route('/services', methods=['GET'])
@app.route('/api/services', methods=['GET'])
def get_service():
    error = False
    service_list = []
    try:
        selection = Service.query.all()
    except:
        error = True
    if error:
        abort(404)
    else:        
        if request.path == '/api/services':
            service_list = [service.format() for service in selection]
            return jsonify({
                'success': True,
                'services': service_list
            }), 200
            
        return render_template('pages/services.html', services=selection)

#----------------------------------------------------
# Handler POST request service
#----------------------------------------------------


@app.route('/services', methods=['POST'])
@app.route('/api/services', methods=['POST'])
def create_service():

    service = {}
    try:
        body = request.get_json()
        name = body.get('name', None)
        source = body.get('source', None)
        destiny = body.get('destiny', None)
        
        new_service = Service(name=name, source=source, destiny=destiny)
        new_service.insert()
        service = Service.query.filter(Service.id == new_service.id).one_or_none()
        
    except:
        abort(404)
     
    finally:
        new_service.close()
        if request.path == '/api/services':

            return jsonify({
                'success': True,
                'services': service.format()
            }), 200

    return render_template('pages/services.html', services=service)

#----------------------------------------------------
# Handler PATCH request service
#----------------------------------------------------

@app.route('/services/<int:service_id>', methods=['PATCH'])
@app.route('/api/services/<int:service_id>', methods=['PATCH'])
def update_service(service_id):

    service = {}
    try:
        body = request.get_json()
        name = body.get('name', None)
        source = body.get('source', None)
        destiny = body.get('destiny', None)
        
        up_service = Service.query.filter(Service.id == service_id).one_or_none()
        up_service.name = name
        up_service.source = source
        up_service.destiny = destiny
        up_service.update()
        service = up_service.format()

    except:
        abort(401)
     
    finally:
        up_service.close()
        if request.path == '/api/services/' + str(service_id):

            return jsonify({
                'success': True,
                'services': service
            }), 200

    return render_template('pages/services.html', services=service)

#----------------------------------------------------
# Handler DELETE request service
#----------------------------------------------------

@app.route('/services/<int:service_id>', methods=['DELETE'])
@app.route('/api/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    service = {}
    try:
        
        service_search = Service.query.filter(Service.id == service_id).one_or_none()
        service = service_search.format()
        service_search.delete() 

    except:
        abort(401)
     
    finally:
        service_search.close()
        if request.path == '/api/services/' + str(service_id):

            return jsonify({
                'success': True,
                'services': service
            }), 200

    return render_template('pages/services.html', services=service)    

#----------------------------------------------------
# Handler GET request person
#----------------------------------------------------


@app.route('/people', methods=['GET'])
@app.route('/api/people', methods=['GET'])
def get_people():
    error = False
    people_list = []
    try:
        selection = Person.query.all()
    except:
        error = True
    if error:
        abort(404)
    else:        
        if request.path == '/api/people':
            people_list = [person.format() for person in selection]
            return jsonify({
                'success': True,
                'person': people_list
            }), 200
            
        return render_template('pages/people.html', people=selection)

#----------------------------------------------------
# Handler POST request person
#----------------------------------------------------


@app.route('/people', methods=['POST'])
@app.route('/api/people', methods=['POST'])
def create_person():

    person = {}
    try:
        body = request.get_json()
        name = body.get('name', None)
        kind = body.get('kind', None)
        email = body.get('email', None)
        ratew = body.get('ratew', None)
        rateh = body.get('rateh', None)
        
        new_person = Person(name=name, kind=kind, email=email, ratew=ratew, rateh=rateh)
        new_person.insert()
        person = Person.query.filter(Person.id == new_person.id).one_or_none()
        
    except:
        abort(404)
     
    finally:
        new_person.close()
        if request.path == '/api/people':

            return jsonify({
                'success': True,
                'person': person.format()
            }), 200

    return render_template('pages/people.html', people=person)

#----------------------------------------------------
# Handler PATCH request person
#----------------------------------------------------

@app.route('/people/<int:person_id>', methods=['PATCH'])
@app.route('/api/people/<int:person_id>', methods=['PATCH'])
def update_person(person_id):

    person = {}
    try:
        body = request.get_json()
        ratew = body.get('ratew', None)
        rateh = body.get('rateh', None)
        
        up_person = Person.query.filter(Person.id == person_id).one_or_none()
        up_person.ratew = ratew
        up_person.rateh = rateh
        up_person.update()
        person = up_person.format()

    except:
        abort(401)
     
    finally:
        up_person.close()
        if request.path == '/api/people/' + str(person_id):

            return jsonify({
                'success': True,
                'person': person
            }), 200

    return render_template('pages/people.html', people=person)

#----------------------------------------------------
# Handler DELETE request person
#----------------------------------------------------

@app.route('/people/<int:person_id>', methods=['DELETE'])
@app.route('/api/people/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = {}
    try:
        
        person_search = Person.query.filter(Person.id == person_id).one_or_none()
        person = person_search.format()
        person_search.delete() 

    except:
        abort(401)
     
    finally:
        person_search.close()
        if request.path == '/api/people/' + str(person_id):

            return jsonify({
                'success': True,
                'person': person
            }), 200

    return render_template('pages/people.html', people=person)    



# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
