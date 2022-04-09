
class Matematica():
    
    def __init__(self,numerador,denominador):
        #self.algo (la variable llamada algo se vuelve global)
        #constructor
        self.numerador=numerador
        self.denominador=denominador
        self.respuesta=0
        

    def minimafraccion(self):
        numerador = self.numerador
        denominador= self.denominador   
        
        menor=0
        
        if self.numerador<self.denominador:
            menor=numerador
        else:
            menor=denominador

        bandera=True
        contador=2
        while bandera:
            modulonumerador=numerador%contador
            modulodenominador=denominador%contador
         
            if modulodenominador == modulonumerador==0:
                retornonumerador=[]
                numerador= numerador/contador
                denominador=denominador/contador
                menor=denominador
                retornonumerador.append(numerador)
                retornonumerador.append(denominador)
                contador = 1 
            
            if contador== menor:
                bandera=False
            contador+=1
        self.respuesta= retornonumerador


    def imprimeminimo(self):
        print( "numerador:" + str(self.respuesta[0]) + "denominador" + str(self.respuesta[1]))


mate=Matematica(9,27)
mate.minimafraccion()
mate.imprimeminimo()


