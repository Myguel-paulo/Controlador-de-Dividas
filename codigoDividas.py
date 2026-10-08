from datetime import date
import mysql.connector

conexao = mysql.connector.connect(host="127.0.0.1", user="root",password="", database="BancoDividas")
cursor = conexao.cursor()


while True:

    print("Escolha uma das opções abaixo: ")
    print("--- --- --- --- --- ---")
    print("1. Registrar sálario")
    print("2. Redefinir sálario")
    print("3. Cadastrar divida")
    print("4. Consultar divida do mês")
    print("--- --- --- --- --- ---")

    decisao = input(int("Digite o número da opção: "))

    match decisao:

        case 1 : 
            

        case _:
            print("ola")
    

    break
