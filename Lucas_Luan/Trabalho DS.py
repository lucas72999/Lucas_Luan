#Lucas_Luan

import mysql.connector

banco = mysql.connector.connect(
    host="10.30.29.100",
    port=3309,
    user="root",
    password="root123",
    database="vinicius_pedro"
) #CONEXÃO
cursor = banco.cursor()

cursor.execute("CREATE database IF NOT EXIST vinicius_pedro")

#BANCO

cursor.execute("CREATE database IF NOT EXIST vinicius_pedro")
cursor.execute("USE vinicus_pedro")

cursor.execute("""
CREATE TABLE IF NOT EXIST Usuario 
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255),
    email  VARCHAR(50),
    senha VARCHAR(100),
    idade INT
""")