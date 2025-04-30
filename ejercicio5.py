num1 = float(input("ingresa un numero: "))
num2 = float(input("ingresa un numero: "))

if num1 > 0 and num2 > 0 :
    print("ambos numeros son positivos")
elif num1 <= 0 and num2 <= 0 :
    print("ambos numeros son negativos")
else :
    print("al menos uno es positivo")