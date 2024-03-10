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