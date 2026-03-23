#Lucas_Luan

import mysql.connector

banco = mysql.connector.connect(
    host="10.30.29.162",
    port=3309,
    user="root",
    password="root123",
    database="lucas_luan"
)

cursor = banco.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS lucas_luan")

#cursor.execute("""

#CREATE TABLE IF NOT EXISTS Usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username Varchar(255),
    email Varchar(50),
    senha Varchar(100),
    idade INT
)
""")
