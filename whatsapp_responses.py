import pandas as pd
data = pd.read_csv("prueba2.csv")
data_dict = data.to_dict('list')

def response(input_message):
    message = input_message.lower()
    skillone = data_dict['skillone']
    skilltwo = data_dict['skilltwo']

    if message == 'continuar':
        return 'Very nice, lets play a Q&A game!'+ '\n'+'Have you worked with ' + str(skillone) + ' ?'
    elif message == 'yes':
        return 'Awesome! Let us know more about your experience.'
    elif message == 'no':
        return 'Unfortunatly, ' + str(skillone) + ' is a required skill for this position.' + 'We have many more open positions that could be of your interest. Please follow this link and appy!'
    else:
        return 'Cool!'