from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

import route

if __name__=='__main__':
    app.run(debug=True)