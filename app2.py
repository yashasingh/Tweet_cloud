
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
	return "Hello World!! Yasha Rocks"

@app.route('/456')
def calc():
	return "this is second function"

if __name__ == '__main__':
	app.run(debug=True)

