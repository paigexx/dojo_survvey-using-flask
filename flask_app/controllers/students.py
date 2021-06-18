from flask_app import app
from flask import redirect, session, render_template, request
from flask_app.models.student import Student


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods =['POST'])
def user_information():
    # dont need to rewrite all the data, just match from the form and on query result and pass the request.form into the function directly
        # data = {
                # "name": request.form["name"],
                # "location": request.form["location"],
                # "language": request.form["language"],
                # "comment": request.form["comment"]
                # }
    # validate data before you call the create student 
    if not Student.validate_data(request.form):
        return redirect('/')
    # right now student = the id number in the terminal 
    student = Student.create_student(request.form)
    # turn that into data to feed the class method function 
    data = {
        "student_id": student
    }
    # reassign the student as the dictionary that comes from the show meethod. WHY? You can access it and use jinja in the template to display the information. 
    student = Student.show_student(data)
    # for my tracking
    print("*********")
    # shows the newly created students dictionary in the terminal! Yay! 
    print(student)

    return render_template("result.html", student = student)