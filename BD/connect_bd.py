import mysql.connector

def connectBD():
    mydb = mysql.connector.connect(
        host="host ip",
        user="username",
        passwd="passwd",
        database="databasename"
        )

    return mydb

connectBD()
