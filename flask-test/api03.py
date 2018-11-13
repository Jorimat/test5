# Inspiration:
# https://www.codementor.io/dushyantbgs/deploying-a-flask-application-to-aws-gnva38cf0

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/goodbye')
def goodbye_world():
    return 'Goodbye, World!'

@app.route('/json-example', methods=['POST']) #GET requests will be blocked
def json_example():
    req_data = request.get_json()
    
    user = req_data['user']
    article = req_data['article']
    utc = req_data['utc']

    return '''
        Collected these data:
            user: {}
            article: {}
            utc: {}'''.format(user, article, utc)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

# Usage:
# Run with $ sudo python3 api.py
# Surf to http://52.31.140.180/
# You should see 'Hello, World!'
