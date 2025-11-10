from controller.criptografia import *
database = {}

#Aqui basicamente vou fazer operações CRUD com uma lista, para evitar baixar dependências como sqlite, prisma (ORM) e etc... E não aumentar muito a complexidade.

def login(email:str, password:str):
    if email in database:
        user = database[email]
        if  check_hash(user['password'],password):
            return True
    
    return False    

def register(name, email, password):
    if email in database:
        raise Exception("E-mail já cadastrado")

    password_hash = generate_hash (password)
    database[email] = {"name": name, "password": password_hash}
    
    return True


# Testes unitários

print(register('marcos','marcossantos8002@gmail.com','123'))
print(database)

print(login('marcossantos8002@gmail.com','123'))