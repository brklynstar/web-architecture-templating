from flask import Flask, request, render_template
import random
from random import randint

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')
    
   

@app.route('/froyo_results')
def show_froyo_results():
    context = {
        'froyo_flavor': request.args.get('flavor'),
        'froyo_toppings': request.args.get('toppings')
    }

    return render_template('froyo_results.html', **context)

  
@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite color? <br/>
        <input type="text" name="color"><br/>
        What is your favorite animal?<br/>
        <input type="text" name= "animal"><br/>
        What is your favorite city? <br/>
        <input type="text" name="city" ><br/>
        <input type="submit" value="Submit!">
    </form>
    """
@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    users_fav_color =request.args.get('color')
    users_fav_animal =request.args.get('animal')
    users_fav_city = request.args.get('city')
    return f'Wow, I didnt know {users_fav_color} {users_fav_animal}s lived in {users_fav_city}!'
    

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/secret_message" method="POST">
        Enter your secret message <br/>
        <input type="text" name="message"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    users_message = request.form.get('message')
    return f'Here is your secret message! {sort_letters(users_message)}'
    
    

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')

    

@app.route('/calculator_results/')
def calculator_results():
    """Shows the user the result of their calculation."""
    number1 = int(request.args.get('operand1'))
    number2 = int(request.args.get('operand2'))
    operator = request.args.get('operation')
        
    if operator == "add":
        result = int(number1 + number2)
    elif operator == "subtract":
        result = int(number1 - number2)
    elif operator == "multiply":
        result = int(number1 * number2)
    elif operator == "divide":
        result = int(number1 / number2)
    
    context = {
        'number1' : number1,
        'number2' : number2,
        'operator' : operator,
        'result' : result,
    }

    return render_template('calculator_results.html')

HOROSCOPE_PERSONALITIES = {
    'aries': 'adventurous and energetic',
    'taurus': 'patient and reliable',
    'gemini': 'adaptable and versatile',
    'cancer': 'emotional and loving',
    'leo': 'generous and warmhearted',
    'virgo': 'modest and shy',
    'libra': 'easygoing and sociable',
    'scorpio': 'determined and forceful',
    'sagittarius': 'intellectual and philosophical',
    'capricorn': 'practical and prudent',
    'aquarius': 'friendly and humanitarian',
    'pisces': 'imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""

    # TODO: Get the sign the user entered in the form, based on their birthday
    users_name = request.args.get('users_name')
    horoscope_sign = request.args.get('horoscope_sign')

    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    if horoscope_sign == 'aries':
        users_personality = 'adventerous and energetic'
    elif horoscope_sign == 'taurus':
        users_personality = 'patient and reliable'
    elif horoscope_sign == 'gemini':
        users_personality = 'adaptable and versatile'
    elif horoscope_sign == 'cancer':
        users_personality = 'emotional and loving'
    elif horoscope_sign == 'leo':
        users_personality = 'generous and warmhearted'
    elif horoscope_sign == 'virgo':
        users_personality = 'modest and shy'
    elif horoscope_sign == 'libra':
        users_personality = 'easygoing and sociable'
    elif horoscope_sign == 'scorpio':
        users_personality = 'determined and forceful'
    elif horoscope_sign == 'sagittarius':
        users_personality = 'intellectual and philosophical'
    elif horoscope_sign == 'capricorn':
        users_personality = 'practical and prudent'
    elif horoscope_sign == 'aquarius':
        users_personality = 'friendly and humanitarian'
    elif horoscope_sign == 'pisces':
        users_personality = 'imaginative and sensitive'

    

    # TODO: Generate a random number from 1 to 99
    lucky_number = randint(1,99)

    context = {
        'horoscope_sign': horoscope_sign,
        'users_personality': users_personality, 
        'users_name': users_name,
        'lucky_number': lucky_number,
        
    }

    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)

