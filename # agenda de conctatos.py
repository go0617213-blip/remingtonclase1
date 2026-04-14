# agenda de conctatos

agenda=[]
while True:
    nombre=input("ingrese el nombre del conctato:")
    if nombre in agenda:
        print("el conctato ya existe")
    else: 
        telefono=input("ingrese el telefono:")
        agenda[nombre]=telefono
    print(agenda)
    
