from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")


@app.route("/application-form")
def application_page():
    """Displays the application"""

    return render_template("application_form.html")


@app.route("/application", methods=["POST"])
def application_confirmation():
    """Confirms application receipt."""

    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    job = request.form.get("job")
    salary = request.form.get("salary")

    return render_template("application_response.html",
           firstname=firstname, lastname=lastname,
           job=job, salary=salary)


if __name__ == "__main__":
    app.run(debug=True)
