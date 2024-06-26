Ejercicio  1 :

 fecha de clase :
    def  init ( self , dia = Ninguno , mes = Ninguno , anio = Ninguno ):
        si  dia  es  Ninguno  o  mes  es  Ninguno  o  anio  es  Ninguno :
            hoy  =  fecha . hoy ()
            ser . día  =  hoy . día
            ser . mes  =  hoy . yo
            yo mismo . año  =  hoy . año
        demás :
            ser . dia  =  dia
            ser . mes  =  mes
            ser . año  =  año
        ser . fecha  =  fecha ( self . año , self . mes , self . dia )

    def  calcular_dif_fecha ( self , otra_fecha ):
        si  no es  instancia ( otra_fecha , Fecha ):
            rise  TypeError ( "El argumento debe ser una instancia de la clase Fecha" )
        return  abs (( self . fecha  -  otra_fecha . fecha ). días )

    def  str ( yo mismo ):
        return  f" { self . dia :02d } / { self . mes :02d } / { self . año } "

    def  add ( yo , días ):
        si  no es  instancia ( días , int ):
            rise  TypeError ( "El argumento debe ser un número entero" )
        nueva_fecha  =  yo . fecha  +  timedelta ( dias = dias )
        return  Fecha ( nueva_fecha . día , nueva_fecha . mes , nueva_fecha . año )

    def  eq ( self , otra_fecha ):
        si  no es  instancia ( otra_fecha , Fecha ):
            rise  TypeError ( "El argumento debe ser una instancia de la clase Fecha" )
        regresar  a uno mismo . fecha  ==  otra_fecha . fecha


Ejercicio  2 :


 Alumno de la clase :
    def  init ( self , nombre , dni , fecha_ingreso , carrera ):
        ser . datos  = {
            "Nombre" : nombre ,
            "DNI" : dni ,
            "FechaIngreso" : fecha_ingreso ,
            "Carrera" : carrera
        }

    def  cambiar_datos ( self , ** kwargs ):
        para  clave , valor  en  kwargs . elementos ():
            si  ingresas la clave  en  self . datos :
                ser . datos [ clave ] =  valor

    def  antigüedad ( yo ):
        fecha_ingreso  =  self . datos [ "FechaIngreso" ]
        si  es instancia ( fecha_ingreso , str ):
            fecha_ingreso  =  fechahora . strptime ( fecha_ingreso , "%Y-%m-%d" ). fecha ()
        hoy  =  fecha . hoy ()
        retorno ( hoy  -  fecha_ingreso ). días  //  365

    def  str ( yo mismo ):
        return  f"Alumno( { self . datos } )"

    def  eq ( yo , otro ):
        si  es instancia ( otro , alumno ):
            devolverte  a ti mismo . datos [ "DNI" ] ==  otro . datos [ "DNI" ]
         falso retorno


Ejercicio  3 :


importar  aleatoriamente

 Alumno de la clase :
    def  init ( self , nombre , edad , promedio ):
        ser . nombre  =  nombre
        ser . edad  =  edad
        ser . promedio  =  promedio

    def  str ( yo ):
        return  f"Nombre: { self . nombre } , Edad: { self . edad } , Promedio: { self . promedio } "

clase  Nodo :
    def  inicio ( self , alumno = Ninguno ):
        ser . alumno  =  alumno
        ser . siguiente  =  Ninguno
        yo mismo anterior  =  Ninguno

clase  ListaIterador :
    def  inicio ( self , cabeza ):
        ser . real  =  cabeza

    definidor  ( yo)) :
        regresar  a uno mismo

    def  siguiente ( yo ):
        si  uno mismo . reales  es  Ninguno :
            elevar  StopIteration
        demás :
            nodo  =  yo . actual
            ser . real  =  yo . actual . siguiente
            volver  nodo . alumno

clase  ListaDoblementeEnlazada :
    definición  de inicio ( auto ):
        yo mismo.cabeza =  Ninguno 
        yo mismo.cola =  Ninguno 

    def  esta_vacia ( auto ):
        devuelve  self . cabeza  es  Ninguno

    def  insertar_al_final ( self , alumno ):
        nuevo_nodo  =  Nodo ( alumno )
        si  uno mismo . esta_vacia ():
            ser . cabeza  =  nuevo_nodo
            ser . cola  =  nuevo_nodo
        demás :
            nuevo_nodo . anterior  =  yo . reajuste salarial
            ser . cola . siguiente  =  nuevo_nodo
            ser . cola  =  nuevo_nodo

    def  eliminar ( self , alumno ):
        real  =  yo . cabeza
        encontrado  =  falso
        mientras que  real  no es  Ninguno y no se encuentra :    
            si es  real . alumno  ==  alumno :
                encontrado  =  Verdadero
            demás :
                real  =  real . siguiente

        si  real  es  Ninguno :
            rise  ValueError ( "El alumno no está en la lista" )
        elif  actual  ==  yo . cabeza :
            ser . cabeza  =  actual . siguiente
            si  uno mismo . cabeza  no es  Ninguno : 
                ser . cabeza . anterior  =  Ninguno
        elif  actual  ==  yo . cola :
            yo mismo.cola =  actual.anterior 
            ser . cola . siguiente  =  Ninguno
        demás :
            actual . anteriores . siguiente  =  actual . siguiente
            actual . siguiente . anterior  =  real . anterior

    definidor  ( yo)) :
        return  ListaIterador ( self . cabeza )

    def  lista_ejemplo ( self , n ):
        nombres  = [ "Juan" , "María" , "Pedro" , "Ana" , "Luisa" ]
        lista  =  ListaDoblementeEnlazada ()
        para  _  en el  rango ( n ):
            nombre  =  aleatorio . elección ( nombres )
            edad  =  aleatoria . randint ( 18 , 25 )
            promedio  =  ronda ( aleatorio . uniforme ( 6 , 10 ), 2 )
            alumno  =  alumno ( nombre , edad , promedio )
            lista . insertar_al_final ( alumno )
        volver  lista


Ejercicio  4 :


 Alumno de la clase :
    def  _init_ ( self , nombre , fecha_ingreso ):
        ser . nombre  =  nombre
        ser . fecha_ingreso  =  fecha_ingreso
        ser . siguiente  =  Ninguno
        yo mismo anterior  =  Ninguno

clase  ListaDoblementeEnlazada :
    def  _init_ ( yo ):
        yo mismo.cabeza =  Ninguno 
        yo mismo.cola =  Ninguno 

    def  insertar_alumno ( self , nombre , fecha_ingreso ):
        nuevo_alumno  =  Alumno ( nombre , fecha_ingreso )
        si  uno mismo . cabeza  es  Ninguno :
            ser . cabeza  =  nuevo_alumno
            ser . cola  =  nuevo_alumno
        demás :
            nuevo_alumno . anterior  =  yo . reajuste salarial
            self.cola.siguiente = nuevo_alumno  
            ser . cola  =  nuevo_alumno

    def  ordenar_por_fecha_ingreso ( self ):
        si  uno mismo . cabeza  es  Ninguno :
            devolver

        def  insertar_en_orden ( nodo ):
            real  =  yo . cabeza

            mientras que  actual  no es  Ninguno y actual . fecha_ingreso < nodo . fecha_ingreso :     
                real  =  real . siguiente

            si  real  es  Ninguno :
                nodo . anterior  =  yo . reajuste salarial
                ser . cola . siguiente  =  nodo
                ser . cola  =  nodo
            elif  actual . anterior  es  Ninguno :
                nodo . siguiente  =  yo . cabeza
                ser . cabeza . anterior  =  nudo
                yo mismo.cabeza =  nudo 
            demás :
                nodo . anterior  =  real . anterior
                nodo . siguiente  =  actual
                actual . anteriores . siguiente  =  nodo
                actual . anterior  =  nudo

        lista_ordenada  =  Ninguno
        real  =  yo . cabeza

        mientras que  real  no es  Ninguno : 
            siguiente  =  actual . siguiente
            actual . anterior  =  Ninguno
            actual . siguiente  =  Ninguno
            insertar_en_orden ( actual )
            actual  =  siguiente

        real  =  yo . cabeza
        mientras que  real . anterior  no es  Ninguno : 
            real  =  real . anterior
        ser . cabeza  =  real

        real  =  yo . reajuste salarial
        mientras que  real . siguiente  no es  Ninguno : 
            real  =  real . siguiente
        ser . cola  =  real

    def  imprimir_lista ( self ):
        actual  =  yo . cabeza
        mientras que  real  no es  Ninguno : 
            print ( f"Nombre: { actual . nombre } , Fecha de ingreso: { actual . fecha_ingreso } " )
            real  =  real . siguiente


Ejercicio  5 :


importar  sistema operativo

def  crear_directorio_y_archivo ( ruta_directorio , nombre_archivo , lista_alumnos ):
    intentar :
        os . makedirs ( ruta_directorio , exist_ok = True )

        con  open ( os.path.join ( ruta_directorio , nombre_archivo ) , ' w ' ) como f :​ 
            para  alumno  en  lista_alumnos :
                F.​ escribe ( f" { alumno } \n " )

        print ( f"Archivo ' { nombre_archivo } ' creado exitosamente en ' { ruta_directorio } '" )

        volver  ruta_directorio

    excepto  IOError  como  e :
        print ( f"Error al crear el archivo: { e } " )
        regresar  Ninguno
    excepto  OSError  como  e :
        print ( f"Error al crear el directorio: { e } " )
        regresar  Ninguno

def  mover_y_borrar ( ruta_origen , ruta_destino , nombre_archivo ):
    intentar :
        os . cambiar nombre ( ruta_origen , ruta_destino )
        print ( f"Directorio movido de ' { ruta_origen } ' a ' { ruta_destino } '" )

        archivo_a_borrar  =  os . camino . unirse ( ruta_destino , nombre_archivo )
        os . eliminar ( archivo_a_borrar )
        print ( f"Archivo ' { nombre_archivo } ' borrado correctamente" )

        os . rmdir ( ruta_destino )
        print ( f"Directorio ' { ruta_destino } ' borrado correctamente" )

    excepto  FileNotFoundError  como  e :
        print ( f"No se pudo encontrar el archivo o directorio: { e } " )
    excepto  OSError  como  e :
        print ( f"Error al mover o borrar archivos/directorios: { e } " )
