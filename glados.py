from flask import Flask, redirect, url_for, request

from log import *
from get_date import *
from get_weather import *
from no_idea import *

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def all_intents():
    if request.is_json == False:
        return ''
    else:
        return parse_intent(request.get_json())

def parse_intent(content):
    log.debug(content)

    response_speech = ''
    
    if content['intent']['name'] == 'GetTime':
        response_speech = GetTime(content)
    elif content['intent']['name'] == 'GetDate':
        response_speech = GetDate(content)
    elif content['intent']['name'] == 'GetTemperature':
        response_speech = GetTemperature(content)
    else:
        response_speech = NoIdea(content)
    
    return {
        'speech': {
            'text': response_speech
        }
    }
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
