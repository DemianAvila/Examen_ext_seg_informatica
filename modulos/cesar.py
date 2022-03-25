"""
IMPLEMENTACION DEL CIFRADO CESAR
RECIBE UNA SERIE DE OPCIONES DADAS POR EL 
FLUJO PRINCIPAL DEL PROGRAMA, ADEMAS DE UNA FUNCION QUE 
RECORRE LAS LISTAS DEPENDIENDO EL RECORRIMIENTO QUE SE LE DE
"""

def cesar(opciones, recorre_origen):
    #DE LA CADENA DEL MENSAJE DE TEXTO OBTEN SU POSICION EN EL ALFABETO
    indices = list(map(lambda x: opciones["alfabeto_valido"].index(x), opciones["mensaje"]))
    #MODIFICA EL RECORRIDO OBTENIENDO EL MODULO EN CASO DE QUE SEA MAS GRANDE QUE EL ALFABETO
    opciones["desplazamiento"] = opciones["desplazamiento"]%len(opciones["alfabeto_valido"])
    #SUMA LOS LUGARES DEL DESPLAZAMIENTO A LOS INDICES
    indices = list(map(lambda x: x+opciones["desplazamiento"] ,indices))
    #OBTEN EL MODULO DE CADA UNA DE LAS POSICIONES CON RESPECTO AL TAMAÑO DEL ALFABETO PARA EVITAR DESBORDAMIENTOS
    indices = list(map(lambda x: x%len(opciones["alfabeto_valido"]) ,indices))
    #APLICA EL CIFRADO
    cifrado = []
    for index in indices:
        cifrado.append(opciones["alfabeto_valido"][index])
    
    cifrado = "".join(cifrado)
    print(cifrado)
    return cifrado