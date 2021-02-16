import os
from flask import Flask, request, abort, render_template, jsonify
from models import setup_db
from flask_bootstrap import Bootstrap
from flask_cors import CORS

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    setup_db(app)    
    CORS(app)


    



    @app.route('/')
    def index():
      gretting = "Hello Word"
      return render_template('pages/home.html', gretting=gretting)

    return app


app = create_app()

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
