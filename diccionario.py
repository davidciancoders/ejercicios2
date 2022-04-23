from this import d





usuario="señora"
password="123456"

dicusuario={usuario:password, "señora2":"654871", "cliente":"asdfasdf"}

def imprimediccionario(diccionario):
    impresiondiccionario=""
    for keys in diccionario:
        impresiondiccionario+=keys+ " - " + diccionario[keys] + " " 

    #print(impresiondiccionario)

imprimediccionario(dicusuario)


class persona():

    def correr():
        pass
    def caminar():
        pass


class persona():
    colordepelo=""
    pies=""

class persona2():
    def __init__(self,colordepelo,pies):
        self.colordepelo=colordepelo
        self.pies=pies

    
pers=persona()
print(pers.colordepelo)

pers2=persona2("gris",2)
print(pers2.colordepelo)



    






