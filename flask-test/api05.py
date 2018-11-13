# Inspiration:
# https://www.codementor.io/dushyantbgs/deploying-a-flask-application-to-aws-gnva38cf0
# https://scotch.io/bar-talk/processing-incoming-request-data-in-flask

# Send user, article and utc as a json string (e.g. with Postman)
# This code sends it back, and adds a line to the file events.csv
# String cleaning
# Popularity recommender (in separate file)

# Remark: very inefficient, because every recommendations request requires us to read from disk.  Better: keep events or recommendations in memory, and update with every new event


from flask import Flask, request
import os
import re
import recommender as rec

app = Flask(__name__)

#PARAMETERS
fileOut = 'events.csv'


#FUNCTIONS

def cleanstring(s):
    s = "".join([c for c in s if c.isalpha() or c.isdigit() or c==' ']).rstrip()
    return s


# START

# Make fileOut with header line if it does not exist
if not os.path.isfile(fileOut):
    with open(fileOut, 'w') as file:
        file.write('#use,article,utc')

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
    
    user = cleanstring(user)
    article = cleanstring(article)
    utc = cleanstring(utc)
    
    with open(fileOut, 'a') as file:
        file.write('\n' + user + ',' + article + ',' + utc)
        
    recommendations = rec.recommend_pop(fileOut)

    return '''
Saved to {}:
    user: {}
    article: {}
    utc: {}
RECOMMENDED:
{}'''.format(fileOut, user, article, utc, str(recommendations))


    
# MAIN
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)


# Usage:
# Run with $ sudo python3 api.py
# Surf to http://52.31.140.180/
# You should see 'Hello, World!'
