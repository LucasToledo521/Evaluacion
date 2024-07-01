vehiculo=[

]





infolista="""-------------------------------------------------------------------
            MENU DE REGISTRO VEHICULOS TALLER MECANICO
        MARCA       AÑO     KILOMETRAJE     COSTO DE REPARACION     IMPUESTOTOTAL
"""





def registro():
            try:
                marca=input("Que marca es su vehiculo\nR:")
                Año=(input("De que año es su vehiculo\nR:"))
                Km=(input("Cuanto kilometraje tiene su vehiculo\nR:"))
                Costo=int(input("Costo de reparacion estimado\nR:"))
                impuesto=Costo*0.08
                Costo_total=Costo+impuesto
                vehiculo.append([marca,Año,Km,Costo,impuesto,Costo_total])
                print("Su registro vehicular se a logrado con exito ")
            except :input("Hubo un error a la hora de escribir intentelo de nuevo porfavor")

def Listar():
      print(f"{infolista}")
      print(vehiculo)

def imprimir():
     a=infolista
     for i in vehiculo:
          input("Cual es la marca de su vehiculo")
     if i in vehiculo:     
         a+f"{vehiculo[0]}"
         a+f"{vehiculo[1]}"
         a +f"{vehiculo[2]}"
         a +=f"{vehiculo[3]}"
         a +=f"{vehiculo[4]}"
         a +f"{vehiculo[5]}"
with open("archivo.txt"'w')as archivo:
     archivo.write(registro)
     
           


while True:
    Menu=input("1-REGISTRAR VEHICULO\n2-LISTAR LOS VEHICULOS\n3-IMPRIMIR ORDEN DE REPARACION\n4- SALIR DEL PROGRAMA\nR:")
    try:
        if Menu=="1":
            registro()
        elif Menu=="2":
            Listar()
        elif Menu=="3":
             imprimir()
        elif Menu=="4":
             exit
    except:print("error")
           

        




