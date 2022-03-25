from modulos.texto_y_opciones import *
from modulos.texto_y_opciones import recorre_origen
from modulos.cesar import *
from modulos.vignere import *

def main():
    #PREGUNTA QUE CIFRADO SE NECESITA
    #NO ADMITE OTRA OPCION
    opcion = 0
    #1 CIFRADO CESAR
    #2 CIFRADO VIGNERE
    while opcion<=0 or opcion>4:
        print("PROGRAMA DE CIFRADO, INGRESE LA OPCIÓN DESEADA")
        print("1.- CRIFRADO CESAR")
        print("2.- CIFRADO VIGENERE")
        print("3.- DESCIFRAR VIGENERE")
        try:
            opcion = int(input())
        except:
            print("OPCIÓN INCORRECTA INTENTE NUEVAMENTE")
        if opcion<=0 or opcion>4:
            print("OPCIÓN INCORRECTA INTENTE NUEVAMENTE")
    #INTRODUCCION DE TEXTO Y OPCIONES 
    opciones = texto_y_opciones(opcion)
    #CIFRADO CESAR
    if opcion==1:
        cesar(opciones, recorre_origen)
    elif opcion==2:
        vignere(opciones, recorre_origen)    
    elif opcion==3:
        desc_vignere(opciones, recorre_origen)
        
if __name__ == "__main__":
   main()