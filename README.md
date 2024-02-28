NOTE MAKING APP✍🏻

Scenario:

A team of enthusiastic data scientists embarked on a mission to develop a Note Taking Application using Python, Flask, and HTML. However, their lack of experience in backend development has led to challenges in making the application fully functional. Recognizing your proficiency in backend development, you have been tasked with fixing the broken code and ensuring the application works seamlessly.


Task:

Refactor the existing codebase and ensure the proper functioning of the Note Taking Application. Document all identified bugs during the debugging process. Remember, the task is not about recreating the app from scratch. Your goal is to fix the already existing codebase and make the application work as intended.

The following code snippet represents the initial state of  Flask application, which contains identifiable bugs impacting its functionality.

# Python Code 

from flask import Flask, render_template, request 


app = Flask(__name__)


notes = []

@app.route('/', methods=["POST"])

def index():

        note = request.args.get("note")
        
        notes.append(note)
        
        return render_template("home.html", notes=notes)
        

if __name__ == '__main__':

    app.run(debug=True)


# HTML code

<!DOCTYPE html>

<html lang="en">
        
<head>
        
    <meta charset="UTF-8">
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>Document</title>
    
</head>

<body>
        
    <form action="">
    
        <input type="text" name="note" placeholder="Enter a note">
        
        <button>Add Note</button>
        
    </form>
    
    <ul>
    
    {% for note in notes%}
    
        <li>{{ note }}</li>
        
    {% endfor %}
    
    </ul>
    
    
</body>

</html>






# Here is the representation of the code snippet, illustrating the corrections made to resolve the bugs.

#STEP-1 importing flask
from flask import Flask, render_template, request # (request) used to take query parameters from user interface
                                                # (render_template) for html

#STEP-2 Init a flask object with __name__ parameter 
app = Flask(__name__)

# STEP-3 Create an end point/route and bind each route with some functionality
notes = []
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note", "")
        notes.append(note)
    return render_template("home.html", notes=notes)

#STEP-4 Run the app
if __name__ == '__main__':
    app.run(debug=True)





<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1> ADD A NOTE:</h1>
    <form action="/" method="POST">
        <input type="text" name="note" placeholder="Enter a note">
        <button type="submit">Add Note</button>
    </form>

    <h3>Your Notes:</h3>
    <ul>
    {% for note in notes%}
        <li>{{ note }}</li>
    {% endfor %}
    </ul>
    
</body>
</html>


