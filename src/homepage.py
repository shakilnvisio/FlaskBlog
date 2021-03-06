from flask import Flask, render_template,url_for
from src.forms import RegistrationFrom, LoginFrom

app = Flask(__name__)
app.config['SECRET_KEY'] = '1094301bce3759830945f0dff34d7603'
#dummy data
posts= [
    {

        'author': 'Shakil Ahmed',
        'title' : 'Flask Post One',
        'content': 'Starting Post',
        'date_posted': 'April 20, 2018'
    },
    {

        'author': 'Rakin Mahmub',
        'title': 'Flask Post Two',
        'content': 'Ending Post',
        'date_posted': 'April 21, 2018'
    }

]
@app.route('/')
@app.route('/home')
def home():
    # static html where I dont load any data from database
    # return render_template('home.html')

    #pass data to html
   return render_template('homeboot.html', posts=posts) # home page with bootsrap design
    # now whatever the variable name i pass into the argument,
    # for example 'bolgpost', we will have access this variable
    # in our template



@app.route('/about')
def about():
    # for statis web sites this is well enough
    #return render_template('about.html')

    return render_template('about.html', title='About')


@app.route('/register')
def register():
    form = RegistrationFrom()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginFrom()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)