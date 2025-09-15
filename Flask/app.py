from flask import Flask

'''
It create an instance of the Flask class,
which will be your  WSGI application
'''

### WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask Framework. Amazing framework, enjoy it"

@app.route("/index")
def index():
    return "Welcome to the index page."

if __name__=="__main__":
    app.run(debug=True) # help to do changes in running session