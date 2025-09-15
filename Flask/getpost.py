from flask import Flask, render_template, request

# render_template -> helps to redirect the html file to read

'''
It create an instance of the Flask class,
which will be your  WSGI application
'''

### WSGI Application
app = Flask(__name__)


@app.route("/")
def welcome():
    return "<html><h1>Welcome to Flask framework</h1></html>"


@app.route("/index", methods=['GET'])
def index():
    # render_template-> read the folder template then mentioned file
    return render_template('index.html')


@app.route("/about")
def about():
    # render_template-> read the folder template then mentioned file
    return render_template('about.html')


@app.route("/form", methods=['GET', 'POST'])
def form():
    # render_template-> read the folder template then mentioned file
    if request.method == 'POST':
        name=request.form['name']
        email = request.form['email']
        return f'Hello {name}!\nYour mail id is {email}.'

    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)  # help to do changes in running session
