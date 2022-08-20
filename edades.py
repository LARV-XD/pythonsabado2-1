edad=int(input("Digite su edad: "))

if(edad <= 0 or edad >=150):
    print('Usted no existe')
elif(edad>=0 and edad<14):
    print(f'usted es  un niño')
elif(edad>=15 and edad<28):
    print(f'usted es   un joven')
elif(edad>=28 and edad <60):
    print(f'USted es  un adulto')
elif(edad>=60 ):
    print(f'usted es  un viejo')
else:
    print(f'No recozco el dato recibido porfavor digute un opcion valida')