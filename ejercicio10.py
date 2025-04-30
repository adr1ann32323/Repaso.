
edad= int(input("ingresa tu edad: "))

if edad > 1 and edad <= 12:
    print(input("eres un niño"))
elif edad >=13 and edad <= 17:
    print("eres adolescente")
elif edad >=18 and edad <= 59:
    print("eres adulto")
elif edad >= 60 and edad <=90:
    print("eres un anciano ")
else:
    print("tu edad es invalida.")