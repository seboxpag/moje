from bottle import route, run, template

@route('/hello/<name>')
def hello(name):
	return template('Hello {{name}}!', name=name)
	
	
run(host='localhost', port=8080, debug=True)
