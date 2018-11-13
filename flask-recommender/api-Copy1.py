# Inspiration
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

# Make fileOut with header line if it does not exist
if not os.path.isfile(fileOut):
    with open(fileOut, 'w') as file:
        file.write('#use,article,utc')
    


#JSON OBJECTS

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
    app.run(debug=True, port=5000)

    
