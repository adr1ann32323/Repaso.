edad = int(input("dime tu edad: "))
if edad >=0 and edad < 18:
    print("no puedes votar")
elif edad >= 18 and edad <= 90 :
    print("puedes votar")
else:
    print("ingresa una edad valida")