# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Prisha" 
    age = "17" 

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father_webpage():

    name = "Naveen"
    age = "49"

    return render_template("father.html", name = name, age= age)


# define the route to mother webpage
@app.route("/mother")
def mother_webpage():

    name = "Shruti"
    age = "48"

    return render_template("mother.html", name = name, age= age)


# define the route to friends webpage
@app.route("/sister")
def sister_webpage():

    name = "Arshiya"
    age = "21"

    return render_template("sister.html", name = name, age= age)



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
