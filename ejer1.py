primer=35
segundo = 7

menor=0

if primer>segundo:
    menor=segundo
else:
    menor= primer


bandera=True
contador=2
while bandera:
    
    primermodulo= primer%contador
    segundomodulo=segundo%contador
    if (primermodulo==segundomodulo==0):
        primer=primer/contador
        segundo=segundo/contador
        print(contador,primer,segundo)    
        print("eureca")
        menor=menor/contador
        contador=1
    
        
    if (contador+1) == menor:
        bandera=False
    
    contador+=1
    
