import os
from flask import Flask, request
from flask.ext.cors import CORS, cross_origin
from imageverify import main

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def hello():
    user = request.args.get('content')
    # not sure what this does
    
    status = main(user)
    # pass the string to main function
    
    return status

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # port 5000 by default, unless defined otherwise
    app.run(debug=True, host='0.0.0.0', port=port)  
