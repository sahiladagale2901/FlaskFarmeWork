from flask import Flask, render_template

# render_template -> helps to redirect the html file to read

'''
It create an instance of the Flask class,
which will be your  WSGI application
'''

### WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to Flask framework</h1></html>"

@app.route("/index")
def index():
    # render_template-> read the folder template then mentioned file
    return render_template('index.html')

@app.route("/about")
def about():
    # render_template-> read the folder template then mentioned file
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True) # help to do changes in running session