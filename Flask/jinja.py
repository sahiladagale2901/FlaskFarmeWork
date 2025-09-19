from flask import Flask, render_template, request

# render_template -> helps to redirect the html file to read

'''
It create an instance of the Flask class,
which will be your  WSGI application
'''

# Jinja 2 template
'''
{{ }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
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


@app.route("/submit", methods=['GET', 'POST'])
def form():
    # render_template-> read the folder template then mentioned file
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f'Hello {name}!\nYour mail id is {email}.'

    return render_template('form.html')


# Variable Rule
# @app.route("/success/<score>")   #> takes str
@app.route("/success/<int:score>")
def success(score):
    # return f'The marks you got is: {score}'
    return f'The marks you got is: ' + str(score)


@app.route("/result/<int:score>")
def result(score):
    if score >= 50:
        res = "Passed"
    else:
        res = "Failed"

    return render_template('result.html', results=res)


@app.route("/successres/<int:score>")
def successres(score):
    if score >= 50:
        res = "Passed"
    else:
        res = "Failed"

    exp = {'score': score, 'res': res}

    return render_template('result1.html', results=exp)


@app.route("/successif/<int:score>")
def successif(score):
    return render_template('result2.html', results=score)


@app.route("/fail/<int:score>")
def fail(score):
    return render_template('result.html', results=score)


@app.route("/getresults", methods=['POST', 'GET'])
def get_results(score):
    return render_template('result.html', results=score)


if __name__ == "__main__":
    app.run(debug=True)