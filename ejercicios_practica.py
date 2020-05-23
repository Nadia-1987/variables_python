#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2
 
Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

def ej1():
    # Ejercicios de práctica con números

    numero_1 = 10.5
    numero_2 = 20.8

 
    sum = numero_1+numero_2
    print("el resultado de la suma entre",numero_1,"y",numero_2,"es",sum)
    
    resta = numero_1-numero_2
    print("el resultado de la resta entre",numero_1,"y",numero_2,"es",resta)

    multiplicacion = numero_1*numero_2
    print("el resultado de la multiplicacion entre",numero_1,"y",numero_2,"es",multiplicacion)

    division = numero_1/numero_2
    print("el resultado de la division entre",numero_1,"y",numero_2,"es",division)

    exponente = numero_1**numero_2
    print("el resultado de elevar",numero_1,"a la",numero_2,"es",exponente)
    
      

    



def ej2():
    # Ejercicios de práctica numérica y cadenas
    
    print("ingrese su nombre completo:")
    nombre_completo=str(input())
    
    print("ingrese su dni:")
    dni=int(input())
    
    print("ingrese su edad:")
    edad=int(input())
    
    print("ingrese su altura:")
    altura=float(input())

    print("nombre completo:",nombre_completo,"dni",dni)

    print("nombre completo:",nombre_completo,"tengo",edad,"años","y mido",altura,"mts")
    
    
def ej3():
    # Ejercicios de práctica con cadenas

    print("nombre completo del padre:")
    nombre_padre=str(input())
    a,b=nombre_padre.split(" ")
    print("nombre completo de la madre:")
    nombre_madre=str(input())
    c,d=nombre_madre.split(" ")
    print("nombre completo hijo:")
    nombre_hijo=str(input()) 
    print(nombre_hijo,b,d)


 
    

    

def ej4():
    # Ejercicios de práctica con cadenas
    a = 1
    
    
    
    
    


def ej5():
    # Ejercicios de práctica con cadenas
    a = 1 
       
   
    

if __name__ == '__main__':
    print("Ejercicios de practica")
    #ej1()
    ej2()
    #ej3()
    #ej4()
    #ej5()
