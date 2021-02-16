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
            
        return render_template('pages/services.html', services=services)




# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
