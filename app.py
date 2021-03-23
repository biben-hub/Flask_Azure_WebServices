from DatabaseConnexion import DatabaseConnexion
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_mail import Mail

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/postedmail', methods=["POST", "GET"])
def add_name():
    db = DatabaseConnexion()
    db.create_table()
    if request.method == "POST":
        name = request.form.get('name')
        mail = request.form.get('mail')
        db.insert_data(name, mail)
        db.close()
    return render_template("success.html", message = "success !")

# démarrage de l'application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)