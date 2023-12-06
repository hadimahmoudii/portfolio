from flask import Flask, session, request, redirect, url_for, render_template
import secrets
import mysql.connector
import subprocess

from iptables import rerouteRequest

app = Flask(__name__)

app.secret_key = secrets.token_bytes()

# database
# mydb = mysql.connector.connect(host="192.168.3.1", port="3306", user="fys", passwd="", database="FYS")
mydb = mysql.connector.connect(host="localhost", port="3306", user="fys", passwd="", database="FYS")


@app.route("/", methods=["GET", "POST"])
def login():
    user_ip = request.environ['REMOTE_ADDR']
    if request.method == "POST":
        achternaam = request.form['achternaam']
        ticketnummer = request.form['ticketnummer']

        try:
            mycursor = mydb.cursor()
            mycursor.execute(f""" SELECT klantnummer FROM Passagier WHERE achternaam = '{achternaam}' """)
            klant_nummer = mycursor.fetchall()
            mycursor.close()


            mycursor = mydb.cursor()
            mycursor.execute(f""" SELECT klantnummer FROM Ticket WHERE ticketnummer = '{ticketnummer}' """)
            klant_nummer_ticket = mycursor.fetchall()
            mycursor.close()

            if klant_nummer == klant_nummer_ticket:
                klant_nummer_ticket = int(klant_nummer_ticket[0][0])
                mycursor = mydb.cursor()
                mycursor.execute(f""" SELECT voornaam FROM Passagier WHERE klantnummer = '{int(klant_nummer_ticket)}' """)
                fname = mycursor.fetchall()
                mycursor.close()

                # rerouteRequest(user_ip)
                subprocess.run(['id', '-un'])
                return render_template("wifi.html", fname = fname)

            else:
                error = "Incorrecte naam of ticketnummer"
                return render_template("index.html", error=error)

        except:
            error = "Incorrecte naam of ticketnummer"
            return render_template("index.html", error = error)

    return render_template("index.html")


@app.route("/wifi")
def wifi():
    return render_template("wifi.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/book")
def book():
    return render_template("book.html")

@app.route("/film")
def film():
    return render_template("film.html")

@app.route("/fact")
def fact():
    return render_template("fact.html")


if __name__ == '__main__':
    app.run(debug=True)

