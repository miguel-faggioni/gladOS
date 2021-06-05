from num2words import num2words
from datetime import date, datetime

LANG = 'pt'

months = [
    'janeiro',
    'fevereiro',
    'março',
    'abril',
    'maio',
    'junho',
    'julho',
    'setembro',
    'agosto',
    'outubro',
    'novembro',
    'dezembro'
]

weekdays = [
    'segunda',
    'terça',
    'quarta',
    'quinta',
    'sexta',
    'sábado',
    'domingo'
]

def GetDate(content):
    return_speech = ['Hoje é dia']

    today = date.today()

    return_speech.append(num2words(today.day, lang=LANG))
    return_speech.append('de')
    return_speech.append(months[today.month])
    return_speech.append('de')
    return_speech.append(num2words(today.year, lang=LANG))
    return_speech.append(',')
    return_speech.append(weekdays[today.weekday()])
        
    return ' '.join(return_speech)
    
def GetTime(content):
    return_speech = ['Agora são']

    now = datetime.now()

    if now.hour > 12:
        return_speech.append(num2words(now.hour-12, lang=LANG))
    else:
        return_speech.append(num2words(now.hour, lang=LANG))
    if now.minute > 0:
        return_speech.append('e')
        return_speech.append(num2words(now.minute, lang=LANG))
    if now.hour < 11:
        return_speech.append('da manhã')
    elif now.hour > 19:
        return_speech.append('da noite')
    elif now.hour > 15:
        return_speech.append('da tarde')
    
    return ' '.join(return_speech)
