#Lucas_Luan

import mysql.connector

banco = mysql.connector.connect(
    host="10.30.29.100",
    port=3309,
    user="root",
    password="root123",
    database="vinicius_pedro"
)
 #CONEXÃO

cursor = banco.cursor()

#BANCO

cursor.execute("CREATE database vinicius_pedro")
cursor.execute ("CREATE TABLE Usuario (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255),email  VARCHAR(50),senha VARCHAR(100),idade INT")

nome = input("Digite o nome: ")
email = input("Digite o email: ")
senha = input("Digite a senha: ")
idade = int(input("Digite a idade:" ))

#inserir_dados(id, nome, email, senha, idade)
cursor.execute(f"INSERT INTO Usuario (nome, email, senha, idade) VALUES ('{nome}', '{email}', '{senha}', {idade})")
banco.commit()

cursor.execute('SELECT *FROM Usuario')
usuario = cursor.fetchall