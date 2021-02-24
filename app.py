import os
from flask import Flask, flash, request, abort, render_template, jsonify, url_for, redirect
from models import *
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from forms import *
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
 
    #Temporaly to obtain flash message. Change and delete.
    app.secret_key = 'many random bytes'
    
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

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format)

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------
# Endpoints
#----------------------------------------------------

@app.route('/')
def index():
    gretting = "Wellcome to my APP"
    return render_template('pages/home.html', gretting=gretting)

#----------------------------------------------------
# Handler GET request projects
#----------------------------------------------------


@app.route('/projects', methods=['GET'])
@app.route('/api/projects', methods=['GET'])
def get_projects():

    project_list = []
    try:
        selection = Project.query.all()

        if len(selection) == 0:
            flash('There are not projects.')

            
    except Exception as e:
        print(e)        

    finally:
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
        abort(422)
     
    finally:
        if request.path == '/api/projects':
            return jsonify({
                'success': True,
                'projects': project.format()
            }), 200

    return render_template('pages/projects.html', projects=project)

#----------------------------------------------------
# Handler PATCH request project
#----------------------------------------------------

@app.route('/projects/<int:project_id>', methods=['PATCH', 'POST'])
@app.route('/api/projects/<int:project_id>', methods=['PATCH'])
def update_project(project_id):

    project = {}

    body = request.get_json()
    deadline = body.get('deadline', None)
    word_count = body.get('word_count', None)
    hour_count = body.get('hour_count', None)
    rate = body.get('rate', None)
    
    up_project = Project.query.filter(Project.id == project_id).one_or_none()

    if up_project is None:
        abort(404)

    try:
        up_project.deadline = deadline
        up_project.word_count = word_count
        up_project.hour_count = hour_count
        up_project.rate = rate
        up_project.update()
        project = up_project.format()

    except:
        abort(422)
     
    finally:
        if request.path == '/api/projects/' + str(project_id):

            return jsonify({
                'success': True,
                'project': project
            }), 200

    return render_template('pages/projects.html', projects=project)

#----------------------------------------------------
# Handler DELETE request project
#----------------------------------------------------

@app.route('/projects/<int:project_id>', methods=['DELETE', 'POST'])
@app.route('/api/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project= {}

    project_search = Project.query.filter(Project.id == project_id).one_or_none()
    
    if project_search is None:
        abort(404)

    try: 
        project = project_search.format()
        project_search.delete() 
        
    except:
        abort(422)
     
    finally:
        if request.path == '/api/projects/' + str(project_id):

            return jsonify({
                'success': True,
                'projects': project
            }), 200

    return render_template('pages/projects.html', projects=project)    

#----------------------------------------------------
# Handler GET request detail service
#----------------------------------------------------


@app.route('/services/<int:service_id>', methods=['GET'])
@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_detail_service(service_id):     
    form = ServiceForm()
    service = Service.query.filter(Service.id == service_id).one_or_none()
    
    if service is None:
        abort(404)

    if request.path == '/api/services/' + str(service_id):
        return jsonify({
            'success': True,
            'person': service
        }), 200

    return render_template('forms/edit_service.html', service=service, form=form)


#----------------------------------------------------
# Handler GET request service
#----------------------------------------------------


@app.route('/services', methods=['GET'])
@app.route('/api/services', methods=['GET'])
def get_services():
    error = False
    service_list = []
    try:
        selection = Service.query.all()

        if len(selection) == 0:
            flash('There are not services.')

            
    except Exception as e:
        print(e)        

    finally:      
        if request.path == '/api/services':
            service_list = [service.format() for service in selection]
            return jsonify({
                'success': True,
                'services': service_list
            }), 200
            
        return render_template('pages/services.html', services=selection)
#----------------------------------------------------
# Handler GET form to create service
#----------------------------------------------------

@app.route('/services/create', methods=['GET'])
def add_new_service():     
    form = ServiceForm()
    return render_template('forms/add_service.html', form=form)


#----------------------------------------------------
# Handler POST request service
#----------------------------------------------------


@app.route('/services', methods=['POST'])
@app.route('/api/services', methods=['POST'])
def create_service():
    form = ServiceForm(request.form)
    service_list = []
    service = {}
    name = {}
    source = {}
    destiny = {}
    
    try:
        if request.path == '/api/services':
            body = request.get_json()
            name = body.get('name', None)
            source = body.get('source', None)
            destiny = body.get('destiny', None)
        else:
            name = request.form.get('name')
            source = request.form.get('source')
            destiny = request.form.get('destiny')            

        if form.validate_on_submit():
            new_service = Service(name=name, source=source, destiny=destiny)
            new_service.insert()
            service = Service.query.filter(Service.id == new_service.id).one_or_none()
            flash("The new service was created successfully!")
        else:
            flash("Something was wrong. Please try again.")       

        services = Service.query.all()
        
        if len(services) == 0:
            flash("There are not services.")
        
        service_list = [service.format() for service in services]

    except:
        abort(422)
     
    finally:
        if request.path == '/api/services':
            return jsonify({
                'success': True,
                'services': service.format()
            }), 200

    return render_template('pages/services.html', services=service_list)

#----------------------------------------------------
# Handler PATCH request service
#----------------------------------------------------

@app.route('/services/<int:service_id>', methods=['POST', 'PATCH'])
@app.route('/api/services/<int:service_id>', methods=['PATCH'])
def update_service(service_id):
    form = ServiceForm(request.form)
    service = {}
    name = {}
    source = {}
    destiny = {}
    
    
    if request.path == '/api/services/' + str(service_id):
        body = request.get_json()
        name = body.get('name', None)
        source = body.get('source', None)
        destiny = body.get('destiny', None)
    else:
        name = request.form.get('name')
        source = request.form.get('source')
        destiny = request.form.get('destiny')

    up_service = Service.query.filter(Service.id == service_id).one_or_none()
    
    if up_service is None:
        abort(404)
        
    try:
        if form.validate_on_submit(): 
            up_service.name = name
            up_service.source = source
            up_service.destiny = destiny
            up_service.update()
            service = up_service.format()
            flash("The data was updated successfully!")
        else:
            service = up_service.format()
            flash("Please, try again.")          
            
    except:
        abort(422)
     
    finally:
        if request.path == '/api/services/' + str(service_id):
            return jsonify({
                'success': True,
                'services': service
            }), 200

    return render_template('forms/edit_service.html', service=service, form=form)

#----------------------------------------------------
# Handler DELETE request service
#----------------------------------------------------

@app.route('/services/<int:service_id>', methods=['DELETE', 'POST'])
@app.route('/api/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    service = {}
    service_search = Service.query.filter(Service.id == service_id).one_or_none()
    
    if service_search is None:
        abort(404)

    try:
        service = service_search.format()
        service_search.delete() 

    except:
        abort(422)
     
    finally:
        if request.path == '/api/services/' + str(service_id):
            return jsonify({
                'success': True,
                'services': service
            }), 200

    return render_template('pages/services.html', service=service)    

#----------------------------------------------------
# Handler GET request detail person
#----------------------------------------------------


@app.route('/people/<int:person_id>', methods=['GET'])
@app.route('/api/people/<int:person_id>', methods=['GET'])
def get_detail_person(person_id):     
    form = PersonForm()
    person = Person.query.filter(Person.id == person_id).one_or_none()
    
    if person is None:
        abort(404)

    if request.path == '/api/people/' + str(person_id):
        return jsonify({
            'success': True,
            'person': person
        }), 200

    return render_template('forms/edit_person.html', person=person, form=form)

#----------------------------------------------------
# Handler GET request person
#----------------------------------------------------


@app.route('/people', methods=['GET'])
@app.route('/api/people', methods=['GET'])
def get_people(): 
    people_list = []
    try:
        selection = Person.query.all()

        if len(selection) == 0:
            flash('There are not people.')
        
        people_list = [person.format() for person in selection]
            
    except:
        abort(422)       

    finally:      
        if request.path == '/api/people':
            return jsonify({
                'success': True,
                'person': people_list
            }), 200
            
    return render_template('pages/people.html', people=selection)

#----------------------------------------------------
# Handler GET form to create person
#----------------------------------------------------

@app.route('/people/create', methods=['GET'])
def add_new_person():     
    form = PersonForm()
    return render_template('forms/add_person.html', form=form)

#----------------------------------------------------
# Handler POST request person
#----------------------------------------------------


@app.route('/people', methods=['POST'])
@app.route('/api/people', methods=['POST'])
def create_person():
    form = PersonForm(request.form)
    people_list = []
    person={}
    name={}
    kind={}
    email={}
    ratew={}
    rateh={}
    try:   
        if request.path == '/api/people/':
            body = request.get_json()
            name = body.get('name', None)
            kind = body.get('kind', None)
            email = body.get('email', None)
            ratew = body.get('ratew', None)
            rateh = body.get('rateh', None)
        else:
            name = request.form.get('name')
            kind = request.form.get('kind')
            email = request.form.get('email')
            ratew = request.form.get('ratew')
            rateh = request.form.get('rateh')
       
        if form.validate_on_submit():
            new_person = Person(name=name, kind=kind, email=email, ratew=ratew, rateh=rateh)
            new_person.insert()
            person = Person.query.filter(Person.id == new_person.id).one_or_none()
            flash("The new person was created successfully!")
        else:
            flash("Something was wrong. Please try again.")

        people = Person.query.all()

        if len(people) == 0:
            flash('There are not people.')

        people_list = [person.format() for person in people]        

    except:
        abort(422)
     
    finally:        
        if request.path == '/api/people':
            return jsonify({
                'success': True,
                'person': person.format()
            }), 200

    return render_template('pages/people.html', people=people_list)

#----------------------------------------------------
# Handler PATCH request person
#----------------------------------------------------

@app.route('/people/<int:person_id>', methods=['POST', 'PATCH'])
@app.route('/api/people/<int:person_id>', methods=['PATCH'])
def update_person(person_id):
    form = PersonForm(request.form)   
    person = {}
    name = {}
    ratew = {}
    rateh = {}
        
    if request.path == '/api/people/' + str(person_id):
        body = request.get_json()        
        name = body.get('name')
        ratew = body.get('ratew')
        rateh = body.get('rateh')
    else:
        
        name = request.form.get('name')
        ratew = request.form.get('ratew')
        rateh = request.form.get('rateh')

    up_person = Person.query.filter(Person.id == person_id).one_or_none()
    
    if up_person is None:
        abort(404)

    try:
        if form.validate_on_submit(): 
            up_person.name = name
            up_person.ratew = ratew
            up_person.rateh = rateh
            up_person.update()
            person = up_person.format()
            flash("The data was updated successfully!")
        else:
            person = up_person.format()
            flash("Fill with decimal numbers. Please, try again.")
            
    except:
        abort(422)
     
    finally:
        if request.path == '/api/people/' + str(person_id):

            return jsonify({
                'success': True,
                'person': person
            }), 200

    return render_template('forms/edit_person.html', person=person, form=form)

#----------------------------------------------------
# Handler DELETE request person
#----------------------------------------------------

@app.route('/people/<int:person_id>', methods=['DELETE'])
@app.route('/api/people/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = {}
    person_search = Person.query.filter(Person.id == person_id).one_or_none()
    
    if person_search is None:
        abort(404)

    try:
        person = person_search.format()
        person_search.delete()

    except:
        abort(422) 
        
    finally:
        if request.path == '/api/people/' + str(person_id):
            return jsonify({
                'success': True,
                'person': person
            }), 200

    return render_template('pages/people.html', people=person)


#-------------------------------------------
# ERROR Handler
#-------------------------------------------

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False, 
        "error": 400,
        "message": "Bad request"
        }), 400

@app.errorhandler(404)
def not_found(error):    
    if request.path.startswith("/api/"): 
        return jsonify({
            "success": False, 
            "error": 404,
            "message": "Resource Not found"
            }), 404
    else:
        return render_template('errors/404.html'), 404


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False, 
        "error": 422,
        "message": "Unprocessable"
        }), 422

@app.errorhandler(405)
def not_found(error):
    return jsonify({
        "success": False, 
        "error": 405,
        "message": "Method not allowed"
        }), 405

@app.errorhandler(500)
def not_found(error):
    if request.path.startswith("/api/"):    
        return jsonify({
            "success": False, 
            "error": 500,
            "message": "Internal Server Error"
            }), 500
    else:
        return render_template('errors/500.html'), 500


# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
