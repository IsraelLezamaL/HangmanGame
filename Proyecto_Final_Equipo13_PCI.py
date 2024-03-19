"""Este es un programa con el que puedes jugar ahorcado."""
#Proyecto Final Pensamiento Computacional para la Ingeniería.
#Enrique Navarrete García - A01735289
#Israel Lezama López - A01734758
#V.6.23.7-pfpci
#Juego del ahorcado con temática de películas y 4 subtemáticas de diversos géneros para una experiencia personalizada.

#----------------------------------------------_REPETIDOR DE JUEGO_------------------------------------------------------------------

#Sistema de repetición indeterminada (no fija) del juego mientras el usuario lo decida.
#El valor 1 en la variable ans (respuesta) correrá el juego inicialmente sin preguntar al usuario.
#Solicita al usuario su nombre y lo guarda en una variable para una experiencia personalizada.
nombre=input("¿Cuál es tu nombre de usuario?: ")
ans=1
#Mientras que el usuario responda SÍ al final del juego a la opción de reiniciar, el programa se ejecutará desde el inicio.
while ans==1:
    
    #--------------------------------------------------_FUNCIONES_----------------------------------------------------------------
    
    #Funciones generadas para la compresión de líneas del programa.
    #Definidor de películas; recibe un archivo abierto para lectura como parámetro.
    def pelicula (archivo):
        #De acuerdo al archivo electo, convierte cada línea en un elemento de lista.
        listado_peliculas = archivo.readlines()
        #Determina el número de elementos en la lista.
        num_opciones=len(listado_peliculas)
        #Se importa módulo random para seleccón aleatoria de película de acuerdo a la elección de tema del usuario.
        import random
        #Selecciona un elemento de la lista elegida (1-n) y cierra el archivo.
        movie=random.randint(0,num_opciones-1)
        cartelera.close()
        #Devuelve una película escrita (tipo cadena de caracteres) en el listado del archivo seleccionado.
        pelicula_final=listado_peliculas[movie]
    
        return pelicula_final
    
    #Función que nos ayudara a imprimir las diferentes partes del ahorcado según la cantidad de errores que vaya generando el usuario.
    def hangman(vidas):
        if vidas == 6:
            #Cuerda.
            print("+---+\n|   |\n    |\n    |\n    |\n    |") 
        elif vidas == 5:
            #Cuerda,cabeza.
            print("+---+\n|   |\n0   |\n    |\n    |\n    |")
        elif vidas == 4:
            #Cuerda,cabeza,cuerpo.
            print("+---+\n|   |\n0   |\n|   |\n    |\n    |")
        elif vidas == 3:
            #Cuerda,cabeza,cuerpo,brazo.
            print(" +---+\n |   |\n 0   |\n/|   |\n     |\n     |")     
        elif vidas == 2:
            #Cuerda,cabeza,cuerpo,brazo,brazo.
            print(" +---+\n |   |\n 0   |\n/|\  |\n     |\n     |")
        elif vidas == 1:
            #Cuerda,cabeza,cuerpo,brazo,brazo,pie.
            print(" +---+\n |   |\n 0   |\n/|\  |\n/    |\n     |")
        elif vidas == 0:
            #Ahorcado completo, usuario perdió.
            print(" +---+\n |   |\n 0   |\n/|\  |\n/ \  |\n     |")
        #Devuelve un dibujo de acuerdo al número de errores ingresado como parámetro.
        return(" ")
    
    
    #-----------------------------------------------------_INTRODUCCIÓN_-------------------------------------------------------------
    
    print("                              ¡¡Bienvenid@, este es un juego de ahorcado con temática de películas!!                        ")
    print()
    
    print("                                   ¡Prueba tus conocimientos de cine en este divertido juego!                                    ")
    
    print()
    print()
    
    print("¡Hola!",nombre,"¿Estas listo para jugar?")
    print()
    
    print("Indicaciones: Deberás seleccionar el tema que quieras jugar, una vez hagas la elección, tendrás 7 \noportunidades de error para adivinar la película.")
    print()
    print("                                                        ¡¡Buena Suerte!!                                                        ")
    print()
    
    print("                                                      ¡¿Qué quieres jugar?!                                                    ")
    #Le preguntamos al usuario que temática quiere jugar a través de un listado de opciones.
    print("\n1-Superhéroes \n2-Disney y Pixar \n3-Terror \n4-Cinéfilo (Experto) ")
    print()
    #Recibe y guarda como variable la opción seleccionada por el usuario.
    eleccion=int(input("Escribe el número de tu elección: "))
    #Explica al usuario cómo deberá ingresar datos al programa.
    print()
    print("Ingresa tus respuestas una letra por intento, en minúsculas y sin caracteres especiales. :D")
    #--------------------------------------------------_MENÚ DE OPCIONES_--------------------------------------------------------
    #Le indicamos al programa la acción que debe realizar para cualquier posible opción (1,2,3,4,otro).
    #En caso de no seleccionar una opción disponible en el menú, el programa volverá al usuario al menú.
    #Lo anterior, hasta elegir una opción disponible en el menú.
    while eleccion != 1 and eleccion != 2 and eleccion != 3 and eleccion != 4:
        #Alerta de opción no válida.
        print()
        print ("El género seleccionado no se encuentra disponible en nuestras opciones.")
        print()
        print("                                                      ¡¿Qué quieres jugar?!                                                    ")
        #Le preguntamos al usuario que temática quiere jugar a través de un listado de opciones.
        print("\n1-Superhéroes \n2-Disney y Pixar \n3-Terror \n4-Cinéfilo (Experto) ")
        print()
        #Recibe y guarda como variable la opción seleccionada por el usuario.
        eleccion=int(input("(Escribe el número de tu elección): "))
    #Se abrirá el archivo correspondiente a la elección del usuario y se seleccionará una película de este (Opción 1).
    if eleccion == 1:
        cartelera = open ("cartelera_superheroes.txt","r")
        #Uso de la función "pelicula".
        adivinar = pelicula (cartelera)
    #Se abrirá el archivo correspondiente a la elección del usuario y se seleccionará una película de este (Opción 2).
    elif eleccion == 2:
        cartelera = open ("cartelera_disney.txt","r")
        #Uso de la función "pelicula".
        adivinar = pelicula (cartelera)
    #Se abrirá el archivo correspondiente a la elección del usuario y se seleccionará una película de este (Opción 3).
    elif eleccion == 3:
        cartelera = open ("cartelera_terror.txt","r")
        #Uso de la función "pelicula".
        adivinar = pelicula (cartelera)
    #Se abrirá el archivo correspondiente a la elección del usuario y se seleccionará una película de este (Opción 4).
    else:
        cartelera = open ("cartelera_cinefilo.txt","r")
        #Uso de la función "pelicula".
        adivinar = pelicula (cartelera)
    #Hasta este punto, el programa ya ha seleccionado la película a adivinar.
        
    #----------------------------------------_INFORMACIÓN GENERAL DE PELÍCULA ELEGIDA_--------------------------------------------
    
    #Convierte la cadena de caracteres del nombre de la película elegida en una lista de caracteres.
    caracteres_adivinar=list(adivinar)
    #Elimina el último caracter de la lista al tratarse este de un salto de línea.
    caracteres_adivinar.pop(-1)
    #Realiza un conteo de elementos presentes en la lista (cada letra y espacio en la palabra).
    num_lineas=len(caracteres_adivinar)
    #Genera una cadena de caracteres que remplace a cada caracter de la lista caracteres_adivinar por el símbolo _.
    lineas =  "_" * num_lineas
    #Convierte la cadena de caracteres en una lista (equivalente en tamaño a caracteres_adivinar).
    lineas_espaciadas=list(lineas)
    #Cuenta el numero de elementos que representan espacios en el nombre de la película.
    espacios= caracteres_adivinar.count(" ")
    #Si la palabra cuenta con 1 o más espacios entrará al ciclo while.
    while espacios > 0:
        #Determina la posición más cercana al inicio donde haya un espacio en caracteres_adivinar.
        posicion = caracteres_adivinar.index(" ")
        #Cambia el elemento con misma posición en la lista equivalente (lineas_espaciadas) por un espacio.
        lineas_espaciadas [posicion] = (" ")
        #Cambia el espacio identificado por el símbolo $. De no hacerlo, el programa identificaría el mismo infinitamente.
        caracteres_adivinar[posicion]="$"
        #Realiza un conteo de espacios para determinar si volver a entrar al ciclo (1 o más) o no (0).
        espacios= caracteres_adivinar.count(" ")
    #Convierte la lista generada en caracteres separados por espacios.
    lineas_final = " ".join(lineas_espaciadas)
    #Muestra el número total de letras en la película acompañada por un gráfico descriptivo (línea 158).
    print("Su película tiene ",num_lineas - espacios," letras :D.") 
    print()
    #Imprime la última cadena de caracteres generada (cada _ corresponderá a una letra).
    print(lineas_final)
    #Hasta este punto, el usuario podrá determinar el número de letras a adivinar y el número de palabras en el nombre de la película.
    
    #---------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------__Aquí es donde comienza el juego__---------------------------------
    
    #Genera una lista con los caracteres en el nombre de la película seleccionada.
    pelicula_final=list(adivinar)
    #Elimina el último elemento de la lista al tratarse este de un salto de línea.
    pelicula_final.pop(-1)
    print()
    print()
    print("¡ Demuestra que eres un experto del cine salvando a ",nombre," de la horca :O !")
    print()
    print()
    print("                                                  ¡!Que comience el juego!¡                                                      ")
    #Ingresamos la película escogida al azar en una variable para poder manipular cada valor en la lista pelicula_final.        
    palabra=pelicula_final
    #Creamos una variable que irá acumulando las letras que vaya generando el usuario, independientemente de si son correctas o no.
    palabra_completa= ' '
    #Le damos una cantidad de vidas (7) al usuario antes de juntar el ahorcado; parametro de la función hangman.
    vidas=7
    #Creamos un ciclo que se evaluará hasta que el usuario llegue a las 0 vidas y complete el ahorcado.
    #Pedimos al usuario que ingrese letras para adivinar la película según indicaciones previas.
    tu_letra=" "
    #Vamos acumulando las letras ingresadas por el usuario tanto correctas como incorrectas.
    palabra_completa=palabra_completa+tu_letra
    
    #---------------------------------------------_Adivinanza de letras_---------------------------------------------------------------------------
    
    #Convierte el listado pelicula_final en una cadena de caracteres separados por espacios.
    pelicula_nombre="".join(pelicula_final)
    #Contador inicial de intentos de letras ingresadas realizados.
    intentos=0
    #Contador general de veces en que se ha ingresado cualquier caracter en más de una ocasión.
    repeticiones=0
    #Lista inicial vacía que guarda las letras ingresadas por el usuario.
    letras_empleadas=[]
    #Si el usuario tiene más de 0 vidas, podrá intentar adivinar una letra.
    while vidas>0:
        #Acumulador de número de errores.
        errores=0
        #Realizamos un ciclo que evaluará la letra ingresada para cada letra en la película a adivinar.
        for letra in palabra:
            #Este if se encargara de que si la letra introducida por el usuario es correcta, llenara el espacio oculto de esta letra.
            if letra in palabra_completa:
                print(letra,end=" ")
            #Este else se encargara de mantener ocultas las letras secretas
            else:
                print("_",end=" ")
                #Variable de control de errores.
                errores=errores+1
        #Este if se activará al haber adivinado el usuario todas las letras de la palabra y terminará la partida con "break".
        if errores == 0:
            #Impresión de leyenda de victoria y gráfico decorativo de triunfo.
            print("  ==>  ¡Felicidades ",nombre,", has adivinado la película! =D")
            print()
            print()
            print("                    __________________________________           ")
            print("           ________|                          _   _   |________  ") 
            print("           \       |  \    /  |  |\ |  |\ |  |_  |_|  |       /  ") 
            print("            \      |   \/\/   |  | \|  | \|  |_  | \  |      /   ") 
            print("            /      |__________________________________|      \   ") 
            print("           /__________)                            (__________\  ")
            
            break
    #Pedimos al usuario que ingrese letras para adivinar la película. 
        print()
        print()
        #Previo a cada intento, se señalan al usuario sus intentos, errores y repeticiones de letra ingresada actuales.
        print("Has empleado ",intentos-(7-vidas),"intentos con ",7-vidas,"errores y",repeticiones,"repeticiones de letra.")
        print()
        #Maracador de nuevo intento.
        print("***********************************************************************************************************")
        print()
        #Solicita al usuario una letra para evaluar en el ciclo for de la línea 199 - 207.
        tu_letra=input("¡Elige una letra y adivina la película!:")
        #Convierte las letras ingresadas a minúsculas en caso de error del usuario.
        tu_letra=tu_letra.lower()
        #Variable de control de intentos en caso de acierto (se suma a los casos de acierto).
        intentos=intentos+1
        #Comprueba si la letra ingresada ha sido ingresada previamente (si está ya presente en la lista letras_empleadas.)
        #De repetirse, si la letra es incorrecta contará como error, de ser correcta será perdonada.
        repetida=letras_empleadas.count(tu_letra)
        #Determina qué hacer si la letra ya ha sido ingresada.
        if repetida>0:
            #Leyenda de ya ingresada acompañada por la última letra ingresada (valor repetido).
            print("Letra repetida, DE SER CORRECTA no contará como error: ",tu_letra)
            #Variable de control de letras repetidas.
            repeticiones=repeticiones+1
            #Imprime como apoyo un listado de los caracteres ya ingresados convertido en cadena de texto.
            # Los caracteres estarán separados por " a | b ".
            listado_letras=" | ".join(letras_empleadas)
            print("Intentos digitados: ",listado_letras)
        #La letra ingresada es añadida a la lista letras_empleadas.
        letras_empleadas.append(tu_letra)
        #Vamos acumulando las letras ingresadas por el usuario tanto correctas como incorrectas.
        palabra_completa=palabra_completa+tu_letra
        #Si su letra no es correcta ira imprimiendo las partes del ahorcado.
        if tu_letra not in palabra:
            #Variable de control de vidas para parámetro de función hangman.
            vidas=vidas-1
            #Uso de función hangman.
            dibujo_final=hangman(vidas)
            #Impresión de leyenda con vidas restantes.
            print("¡Fallaste ",nombre," ! Te quedan",vidas,"vidas.")
            #Impresión de la figura de ahorcado.
            print(dibujo_final)
            #Variable para control de intentos en caso de error (se suma a los casos de acierto).
            intentos=intentos+1
        
        #Indica como proceder si el usuario a empleado ya todos sus intentos.
        if vidas == 0:
          #Impresión de leyenda de derrota.
          print("¡Lo sentimos ",nombre," completaste el ahorcado y perdiste! =(")
          print()
          #Impresión del nombre correcto de la película a adivinar.
          print("Tu película a adivinar era: ",pelicula_nombre)
          print()
          #Impresión decorativa del ahorcado completo.
          print(hangman(0))
          
    #-----------------------------------------------------_REINICIO DE PARTIDA------------------------------------------------------------------
   
    print()
    print("************************************************************************************************************")
    print()
    #Presenta al usuario la opción de reiniciar el juego automáticamente.
    print(nombre,", ¿Te gustaría volver a intentarlo?")
    #Impresión de menú interactivo; 1 reiniciará el juego y 2 u otro finalizará la partida.
    print("\n1-SÍ, ",nombre," ACEPTA EL RETO \n2-NO, ",nombre,"TUVO SUFICIENTE POR HOY")
    print()
    #Recibe y guarda como variable la opción seleccionada por el usuario.
    ans=int(input("Escribe el número de tu elección: "))
    print()
    print()
    print("************************************************************************************************************")
    print("************************************************************************************************************")
    print()
    
    #-------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------_FINALIZADO :D_---------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------------





