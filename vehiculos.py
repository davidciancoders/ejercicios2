class vehiculo():
    def __init__(self,kilometraje,combustible,velocidad,rpm,hora):
        self.combustible=combustible
        self.velocidad=velocidad
        self.rpm = rpm
        self.hora=hora
        self.kilometraje=kilometraje

    def vertablero(self):        
        print(""" Bienvenido al Tablero de su vehiculo""")
        print("Combustible " + str(self.combustible))
        print("velocidad " + str(self.velocidad))
        print("Rpm " + str(self.rpm))
        print("Hora " + self.hora)
        print("kilometraje " + str(self.kilometraje))
    
    def modificatablero(self,combustible,velocidad,rpm,hora):
        self.combustible=combustible
        self.velocidad=velocidad
        self.rpm = rpm
        self.hora=hora     



class toyotasedan(vehiculo):
    def __init__(self, kilometraje, combustible, velocidad, rpm, hora):
        self.combustible=combustible
        self.velocidad=velocidad
        self.rpm = rpm
        self.hora=hora
        self.kilometraje=kilometraje
    
    def kilometrajerecorrido(self,kilometrajerecorrido):
        self.kilometraje=self.kilometraje+kilometrajerecorrido

    def mostrarrecorrido(self):
        print(self.kilometraje)        
        return self.kilometraje



bandera=True
toyota=toyotasedan(0,50,25,100,"11:30 a.m.")

while bandera:    
    print("1) Modificar tablero")
    print("2) Ver tablero")
    print("3) Mover vehiculo")
    print("4) visualizar kilometraje")
    print("5) salir")   

    opcion= int(input("ingresa una opcion"))
    if opcion==1:
        combustible= int( input("Ingrese el combustible Int"))
        velocidad= int(input("Ingrese el combustible Int"))
        rpm= int(input("Ingrese las RPM int"))
        hora=input("Ingrese la hora")
        toyota.modificatablero(combustible,velocidad,rpm,hora)

    if opcion==2:
        toyota.vertablero()
    
    if opcion==3:
        kilometraje=int(input("Ingrese el kilometraje recorrido"))
        toyota.kilometrajerecorrido(kilometraje)
    
    if opcion==4:
        toyota.mostrarrecorrido()
    
    if opcion==5:
        bandera=False

    
    
    








        
        
        




