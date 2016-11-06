from flask import Flask
import webbrowser
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
	url = "http://127.0.0.1:5000/"
	webbrowser.open(url)
	app.run()
