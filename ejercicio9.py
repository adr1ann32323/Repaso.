nota = float(input("ingresa una nota, entre 0 y 10: "))
if nota >8 and nota <=10:
    print("sobresaliente")
elif nota >=6 and nota <= 8:
    print("aprobado")
elif nota >=0 and nota <6:
    print("reprobo")
else:
    print("nota invalida")
    
