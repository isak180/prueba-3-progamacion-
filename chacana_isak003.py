import csv
def entre(s):
    while True:
        if s < 0:
            print("porcentaje invalido. no puede ser menor de 0 ")
            s =int(input("ingrese el valor denuevo :"))
        elif s > 100:
            print(" el porcentaje no puede ser mayor a 100")
            s =int(input("ingrese nuevamente : "))
        else:
            break

     
def categ(s):    
        if  0 <= s <=25:
            categoria="chiste"
        elif 26<= s <=50:
            categoria="anecdota"
        elif 51<= s <=75:
            categoria="peligro"
        elif 76<= s <=99:
            categoria="atencion"
        elif s == 100:
            categoria="esclavitud"
        print(f"dependiendo del porcentaje se le asigna la categoria {categoria}")
def estadistica():
    total=0
    mayor=0
    for i in lista:
        porcentaje=int(i['efectiivdad'])
        total=total+porcentaje
        if porcentaje > mayor:
            mayor=porcentaje
    cantidad=len(lista)
    promedio=total/cantidad
    print(f"promedio de porcentaje : {promedio}")
    print(f"el plan com mayor efectivdad :{mayor}")
lista=[]

while True:

    print(".-.-.-.-.-.-.-.")
    print(".-.-.-.MENU PRINCIPAL.-.-.-.-.")
    print("1.- Agregar plan")
    print("2.-Listar planes")
    print("3.- Eliminar plan por ID")
    print("4.- Generar bbdd")
    print("5.- Cargar bbdd")
    print("6.- Estadísticas")
    print("0.- Salir.")
        
    op=int(input("ingrese un numero : "))
    if op ==1:
            id=int(input("ingrese la id del plan :"))
            nombre= input("ingrese el nombre :")
            efectividad=int(input("ingrese la efectividad :"))
            entre(efectividad)
            categoria=(efectividad)
            diccionario={'id':id,'nombre':nombre,'efectividad':efectividad}
            lista.append(diccionario)
    elif op ==2:
        for i in lista:
            print("id:",i["id"],"numero:",i["numero"],"nombre:",i["nombre"],"efectividad:",i["efectividad"],"categoria:")
        
        
        
        
    elif op ==3:
        eliminar=int(input("igresar el id a eliminar : "))
        for i in lista:
            if eliminar == i['id']:
                pregunta=input("desea eliminar el plan? (si/no):").lower()
            if pregunta=="si" or pregunta== "s":
                lista.remove(i)
                print("plan eliminado ")
                break
            else:
                print("no esta eliminado")
                
                
        pass
    elif op ==4:
        with open("planes.csv","w",newline="")as planes:
            escritor_csv=csv.writer(planes)
            escritor_csv.writerow(["id","nombre","efectividad","categoria"])
            escritor_csv.writerows(lista)
            print("el arhivo se creo correctamente!")
        pass
    elif op ==5:
        lista.clear
        with open("planes.csv","r",newline="")as planes:
            leercsv=csv.reader(planes)
            
            for i in leercsv:
                lista.append(i)
        lista.pop(0)
        for x in lista:
            print("id:",x['id'],"numero:",x['numero'],"nombre:",x['nombre'],"efectividad:",x['efectividad'],"categoria:")
        
                      
        pass
    elif op ==6:
        estadistica()
        
        pass
    elif op ==0:
            print("progama cerrado correctamente")
            break
    else:
            print("opcion invalida....")
            print("ingrese un numero : ")
            

        
