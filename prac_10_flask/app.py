from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9.0 / 5 + 32


@app.route('/f/<celsius>')
def convert(celsius):
    fahrenheit = celsius_to_fahrenheit(float(celsius))
    return str(fahrenheit)


if __name__ == '__main__':
    app.run()
