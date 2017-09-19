from flask import Flask, request, send_file
from MyCloud import MyCloud
from MyTwitterAPI import MyTwitterAPI
app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello yashi!"

@app.route('/date/')
def date():
	import datetime
	today = datetime.date.today()
	return str(today)	

@app.route('/power/')
def power():
	x = int(request.args.get('x'))
	y = int(request.args.get('y'))
	res = x ** y;
	myrsultinjson = "{'input' : '" + str(x) + " & " + str(y) +"', 'output' : " + str(res) +"}"
	return str(myrsultinjson)

@app.route('/wordcloud/')
def wordcloud():
	query = request.args.get('query')
	twitter = MyTwitterAPI()
	result = twitter.get_tweets(query)
	mc = MyCloud()
	mc.generate(query, result)
	png_file = query + '.png'
	print (png_file)
	return send_file(png_file)

if __name__ == '__main__':
	app.run(debug=True)
