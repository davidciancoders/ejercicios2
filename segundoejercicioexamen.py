def palindromos (numero):
    cadena_numero=str(numero)
    cadenainvertida=cadena_numero[::-1]    

    for x in range(len(cadena_numero)):
        bandera=True
        if cadena_numero[x]!=cadenainvertida[x]:
            return False
    return True


def primo(numero):
    contador=0     
    for x in range(1,numero+1):
        if (numero%x==0):
            contador+=1
    
    if contador >2:
        return False
    else:
        return True



def palindromo(numero,denominador):

    bandera=True
    contador=numero
    resultado = 0
    while bandera:
        if palindromos(contador):
            if primo(contador):
                bandera= False
                resultado=contador
        contador+=1
    
    print("el paliendromo primo es:" + str(resultado))


palindromo(10000,25)