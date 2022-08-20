#entradas del problema

nivelAgua=int(input("Digita el nivel del agua de la presa: "))

#proceso del problema

if(nivelAgua>=0 and nivelAgua<20):
    print(f'El nivel del agua{nivelAgua} es muy bajo')
elif(nivelAgua>=20 and nivelAgua<400):
    print(f'El nivel del agua{nivelAgua} es optimo')
elif(nivelAgua>=400):
    print(f'El nivel del agua{nivelAgua} es muy alto')
else:
    print(f'No recozco el dato recibido porfavor digute un opcion valida')