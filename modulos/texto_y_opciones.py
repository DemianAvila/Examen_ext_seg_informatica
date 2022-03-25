#VALIDA QUE UNA CADENA DE TEXTO TENGA LOS CARACTERES VALIDOS
def validar_texto(cadena, alfabeto):
    for letra in cadena:
        #SI EL CARACTER NO ESTA EN EL ALFABETO, MANDA FALSE
        if letra not in alfabeto:
            return False
    #DE OTRA FORMA, MANDA VERDADERO
    return True


#MANEJA UNA ENTRADA Y DEVUELVE UN OBJETO
#EN EL CASO DE CESAR, PIDE EL MENSAJE Y EL NUMERO DE DESPLAZAMIENTO
def texto_y_opciones(opcion):
    #OBJETO DE RETORNO
    retorno = {}
    retorno["alfabeto_valido"] = [chr(x) for x in range(ord(' '), ord('~') + 1)]
    #SOLICITA LA ENTRADA HASTA QUE SEA VALIDA
    texto_valido = False
    while not texto_valido:
        #INSTRUCCIONES GENERALES
        if opcion!=3:
            print("ESCRIBE LA CADENA QUE DESEES DESCIFRAR")
        else:
            print("ESCRIBE LA CADENA QUE DESEES DESCIFRAR")
        print("SE ADMITE EL MAPA BÁSICO DE CARACTERES DE UNICODE (DESDE EL U+0020 HASTA EL U+007E)")
        try:
            retorno["mensaje"]=input()
        except:
            print("ERROR, ALGUN CARACTER INVALIDO, VUELVE A INTENTARLO")
            print(f"LOS CARACTERES VALIDOS SON {retorno['alfabeto_valido']}")
            continue
        texto_valido = validar_texto(retorno["mensaje"], retorno["alfabeto_valido"])
        if not texto_valido:
            print("ERROR, ALGUN CARACTER INVALIDO, VUELVE A INTENTARLO")
            print(f"LOS CARACTERES VALIDOS SON {retorno['alfabeto_valido']}")
    #CUANDO EL TEXTO SEA VALIDO, PREGUNTA POR LAS OPCIONES ESPECIFICAS DE CADA CIFRADO
    #CUANDO EL CIFRADO ES CESAR, PREGUNTA EL ESPLAZAMIENTO
    if opcion==1:
        retorno["desplazamiento"] = None
        while retorno["desplazamiento"]==None:
            print("ESCRIBE EL NUMERO DE LUGARES A DESPLAZAR")
            try:
                retorno["desplazamiento"] = int(input())
            except:
                print("VALOR ERRONEO, INTENTALO NUEVAMENTE")
    #CUANDO EL CIFRADO ES VIGNERE, SE DEBE INTRODUCIR LA CLAVE
    #LA CLAVE DEBE SER DE LA MISMA LONGITUD QUE LA CADENA
    elif opcion==2 or opcion==3:
        texto_valido = False
        longitud_igual = False
        while not texto_valido or not longitud_igual:
            print("INGRESA LA CLAVE DE CIFRADO")
            try:
                retorno["clave"]=input()
            except:
                print("ERROR, ALGUN CARACTER INVALIDO, VUELVE A INTENTARLO")
                print(f"LOS CARACTERES VALIDOS SON {retorno['alfabeto_valido']}")
                continue
            texto_valido = validar_texto(retorno["clave"], retorno["alfabeto_valido"])
            if not texto_valido:
                print("ERROR, ALGUN CARACTER INVALIDO, VUELVE A INTENTARLO")
                print(f"LOS CARACTERES VALIDOS SON {retorno['alfabeto_valido']}")
            if len(retorno["clave"])!=len(retorno["mensaje"]):
                print("ERROR, LA CLAVE DE CIFRADO Y LA CADENA A CIFRAR DEBEN TENER LA MISMA LONGITUD")
            else:
                longitud_igual = True
    return retorno

#RECORRE EL ORIGEN DE LA LISTA UN NUMERO O UN CARACTER
def recorre_origen(lista, lugares=None, caracter=None):
    if lugares!=None:
        inicio = lista[0:lugares]
        lista = lista[lugares:]+inicio
        return lista
    if caracter!=None:
        indice = lista.index(caracter)
        inicio = lista[0:indice]
        lista = lista[indice:]+inicio
        return lista
    if caracter==None and lugares==None:
        return None