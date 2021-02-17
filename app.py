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
# Handler GET request services
#----------------------------------------------------


@app.route('/services', methods=['GET'])
@app.route('/api/services', methods=['GET'])
def get_services():
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
# Handler POST request services
#----------------------------------------------------


@app.route('/services', methods=['POST'])
@app.route('/api/services', methods=['POST'])
def create_services():

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
# Handler PATCH request services
#----------------------------------------------------

@app.route('/services/<int:service_id>', methods=['PATCH'])
@app.route('/api/services/<int:service_id>', methods=['PATCH'])
def update_services(service_id):

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
# Handler DELETE request services
#----------------------------------------------------

@app.route('/services/<int:service_id>', methods=['DELETE'])
@app.route('/api/services/<int:service_id>', methods=['DELETE'])
def delete_services(service_id):
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
    
    
    

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
