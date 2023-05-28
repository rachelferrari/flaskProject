from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "<h1>Hello World :)</h1>"


if __name__ == '__main__':
    app.run()


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""


@app.route('/f')
@app.route('/f/<celsius>')
def convert_celsius(celsius="0.0"):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return f"Celsius: {celsius}<br>Fahrenheit: {fahrenheit}"
