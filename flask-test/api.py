# Inspiration:
# https://www.codementor.io/dushyantbgs/deploying-a-flask-application-to-aws-gnva38cf0

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

# Usage:
# Run with $ sudo python3 api.py
# Surf to http://52.31.140.180/
# You should see 'Hello, World!'
