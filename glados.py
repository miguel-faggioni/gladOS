from flask import Flask, redirect, url_for, request

from get_date import *

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def all_intents():
    if request.is_json == False:
        return ''
    else:
        return parse_intent(request.get_json())

def parse_intent(content):
    if content['intent']['name'] == 'GetTime':
        return GetTime(content)
    elif content['intent']['name'] == 'GetDate':
        return GetDate(content)
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
