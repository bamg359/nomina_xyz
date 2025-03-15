



##US1/create register

users = []

def createUser():
    user = []
    id = int(input("Ingrese su Documento de identidad"))
    user.append(id)
    user_name = input("Ingrese su nombre")
    user.append(user_name)
    user_last_name = input("Ingrese su apellido")
    user.append(user_last_name)
    phone = input("ingrese su telefono")
    user.append(phone)
    user_email = input("Ingrese su correo electronico")
    user.append(user_email)
    user_password = input("Ingrese su contraseña")
    user.append(user_password)
    users.append(user)

createUser()
createUser()

print(users)

