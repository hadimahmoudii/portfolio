import mysql.connector

mydb = mysql.connector.connect(host="localhost", port="3306", user="fys", passwd="", database="FYS")
print(mydb)

mycursor = mydb.cursor()

achternaam = "Mahmoudi"
ticketnummer = "abc12345"

mycursor.execute(f""" SELECT nummer FROM Passagier WHERE achternaam = '{achternaam}' """)
klant = mycursor.fetchall()

for x in klant:
  print(x)


mycursor.execute(f""" SELECT passagierNr FROM Ticket WHERE ticketnummer = '{ticketnummer}' """)
ticket = mycursor.fetchall()

#for x in ticket:
#  print(x)

if klant == ticket:
  print("mamad")



