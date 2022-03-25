"""
IMPLEMENTACION DEL CIFRADO VIGNERE
RECIBE UNA SERIE DE OPCIONES DADAS POR EL 
FLUJO PRINCIPAL DEL PROGRAMA, ADEMAS DE UNA FUNCION QUE 
RECORRE LAS LISTAS DEPENDIENDO EL CARACTER QUE SE LE DE
"""

def vignere(opciones, recorre_origen):
    #DE LA CADENA DEL MENSAJE DE TEXTO OBTEN SU POSICION EN EL ALFABETO
    indices = list(map(lambda x: opciones["alfabeto_valido"].index(x), opciones["mensaje"]))
    #VARIABLE PARA GUARDAR EL TEXTO CIFRADO
    cifrado=[]
    #POR CADA UNA DE LAS LETRAS DE LA CLAVE, RELOCALIZA LA LISTA I OBTEN EL CIFRADO
    for index, letra_clave in enumerate(opciones["clave"]):
        lista_tmp=recorre_origen(opciones["alfabeto_valido"],
            lugares=None,
            caracter=letra_clave)
        cifrado.append(lista_tmp[indices[index]])
    cifrado = "".join(cifrado)
    print(cifrado)
    return cifrado


def desc_vignere(opciones, recorre_origen):
    #VARIABLE PARA GUARDAR EL TEXTO DESCIFRADO
    descifrado=[]
    for index, letra_clave in enumerate(opciones["clave"]):
        #RECORRER LA LISTA A CADA UNO DE LA CLAVE
        lista_tmp=recorre_origen(opciones["alfabeto_valido"],
            lugares=None,
            caracter=letra_clave)
        #OBTENER EL INDICE DEL ALFABETO CIFRADO
        indice = lista_tmp.index(opciones["mensaje"][index])
        #OBTENER EL CARACTER DEL ALFABETO ORIGINAL
        descifrado.append(opciones["alfabeto_valido"][indice])
    descifrado = "".join(descifrado)
    print(descifrado)
    return descifrado