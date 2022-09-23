from flask import Flask, render_template, request, make_response
import csv
import mail

HOST_NAME = "localhost"
HOST_PORT = 80
app = Flask(__name__)

@app.route("/")
def index():
    with open("mail.csv", mode ='r') as file:
        csvFile = csv.reader(file)
        return render_template("view.html", csv=csvFile)

if __name__ == "__main__":
    mail.getMail()
    app.run(HOST_NAME, HOST_PORT)