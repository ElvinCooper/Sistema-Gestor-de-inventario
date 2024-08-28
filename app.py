from csv import excel
import cx_Oracle
import os, sys
#from wtforms.validators import length


def conectar_db():
    return cx_Oracle.connect(
        user='TRAIN7',
        password='TRAIN7',
        dsn='SID_CR1'
    )


def limpiar_input():
    """
    Esta es una funcion para limpiar la pantalla
    """
    sys.stdout.write('\r')  # mueve el cursor al principio de la línea
    sys.stdout.write(' ' * 80) # limpiar la línea sobreescribiendo con espacios hasta 80 carcteres
    sys.stdout.write('\r') # mueve el cursor al principio de la línea nuevamente
    sys.stdout.flush()


def limpiar_pantalla():
    """ limpiar pantalla """
    if os.name == 'nt':   # Verifica si el sistema operativo es Windows
        os.system('clear')
    else:
        os.system('clear')


def digitar_producto():
    """
    1- Solicita al usuario que ingrese los detalles de un nuevo producto e inserta esos datos en la base de datos INVENTARIO.
    2- Los datos incluyen código, nombre, categoría, cantidad y precio del producto.
    3- La función también maneja la conexión a la base de datos y confirma la inserción.
    4- Después de agregar el producto, cierra la conexión a la base de datos y ofrece al usuario la opción de regresar al menú principal.
    """
    try:
        conexion = conectar_db()
        cursor =  conexion.cursor()

        print('=============================================================')
        print('               AGREGAR NUEVO PRODUCTO                        ')
        print('=============================================================\n')        
        
        codigo    = int(input('Ingrese el código del producto: '))
        nombre    = input('Ingrese el nombre del producto: ')
        categoria = input('Ingrese la categoria del producto: ')
        cantidad  = int(input('Ingrese la cantidad en stock: '))
        precio    = int(input('Ingrese el precio unitario: ' ))

        query = f"INSERT INTO INVENTARIO VALUES ({codigo}, '{nombre}', '{categoria}' , {cantidad}, {precio})\n"
        cursor.execute(query)
        conexion.commit()

        print('Producto agregado exitosamente al inventario\n')
        
    except cx_Oracle.DatabaseError as err:
        print('No fue posible ingresar la informacion a la base de datos')
    except Exception as e:
        print('Ocurrio un error inesperado:', e)
    finally:
        cursor.close()
        conexion.close()

def consultar_productos():
    """
    Esta funcion permite al usuario consultar la información de un producto en la base de datos a partir de su código de identificación.
    Flujo:
    1. Solicita al usuario que ingrese el código del producto.
    2. Realiza una consulta en la base de datos para obtener los detalles del producto con el código proporcionado.
    3. Muestra al usuario los detalles del producto.
    4. Cierra el cursor y la conexión a la base de datos.
    """
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        print('=============================================================')
        print('               CONSULTA DE PRODUCTOS                         ')
        print('=============================================================\n')

        print('[1] - TODOS LOS ARTICULOS')
        print('[2] - BUSCAR POR CODIGO\n')
                
        consulta = int(input('   DIGITE LA OPCION DESEADA: '))
        resultado = []

        if consulta == 1:           
           query = f"SELECT * FROM INVENTARIO"           
        elif consulta == 2:
            id_codigo = int(input('CODIGO DEL PRODUCTO: '))
            query = f"SELECT * FROM INVENTARIO WHERE ID_PRODUCTO = {id_codigo}"
        else:
            print('OPCION INVALIDA')
            return
        
        cursor.execute(query)
        resultado = cursor.fetchall()            
                                
        if resultado:
            for row in resultado:
                codigo      = row[0]
                descripcion = row[1]
                categoria   = row[2]
                cantidad    = row[3]
                precio      = row[4]

                print(f'Descripcion: {descripcion}\nCantidad en stock: {cantidad}\nCategoria: {categoria}\nPrecio: {precio}\n')                
        else:
            print('No se obtuvo ningun resultado con el codigo selecccionado\n\n')                        

    except cx_Oracle.DatabaseError as error_consulta:
        print("Error en la base datos:", error_consulta)
    except Exception as e:
        print('Ocurrio un error inesperado:', e)
    finally:
        cursor.close()
        conexion.close()

def actualizar_productos():
    '''
    Funcion para actualizar productos.
    '''
    try:
        conexion = conectar_db()
        cursor =  conexion.cursor()

        print('============================================================')
        print('               ACTUALIZAR PRODUCTOS                         ')
        print('============================================================\n')

        id_codigo = int(input('Ingrese el codigo del producto: '))
        nombre    = input('Ingrese el nuevo nombre para producto: ')
        categoria = input('Ingrese la nueva categoria para el producto: ')
        cantidad  = int(input('Ingrese la cantidad en stock: '))
        precio    = int(input('Ingrese el nuevo precio unitario: \n'))
        
        query = f"UPDATE INVENTARIO SET DESCRIPCION_PRODUCTO = '{nombre}', CATEGORIA = '{categoria}', CANTIDAD = {cantidad}, PRECIO = {precio} WHERE ID_PRODUCTO = {id_codigo}\n"
        cursor.execute(query)
        conexion.commit()

        print('Producto actualizado exitosamente en el inventario\n')

    except cx_Oracle.DatabaseError as err:
        print('No fue posible actualizar el producto en la base de datos', err)        
    except Exception as e:
        print('Ocurrio un error inesperado:', e)
    finally:
        cursor.close()
        conexion.close()


def eliminar_productos():
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()

        """
        Esta funcion permite al usuario consultar la información de un producto en la base de datos a partir de su código de identificación.
        Flujo:
        1. Solicita al usuario que ingrese el código del producto.
        2. Realiza una consulta en la base de datos para obtener los detalles del producto con el código proporcionado.
        3. Muestra al usuario los detalles del producto.
        4. Cierra el cursor y la conexión a la base de datos.
        """
        print('=============================================================')
        print('               ELIMINAR PRODUCTOS DEL SISTEMA                ')
        print('=============================================================\n')
        
        id_codigo = int(input('Codigo del producto: '))
            
        query = f"SELECT * FROM INVENTARIO WHERE ID_PRODUCTO = {id_codigo}"
        cursor.execute(query)
        resultado = cursor.fetchall()

        if resultado:
            for row in resultado:
                codigo      = row[0]
                descripcion = row[1]
                categoria   = row[2]
                cantidad    = row[3]
                precio      = row[4]

                print(f'Descripcion: {descripcion}\nCantidad en stock: {cantidad}\nCategoria: {categoria}\nPrecio: {precio}\n')
                continuar = input('¿ESTE ES EL ARTICULO QUE DESEA ELIMINAR?  [S/N]: ').lower()
                
                if continuar == 's':  
                   limpiar_pantalla()                 
                   query = f"DELETE FROM INVENTARIO WHERE ID_PRODUCTO = {id_codigo}"
                   cursor.execute(query)
                   conexion.commit()                   

                   print('Producto eliminado exitosamente al inventario\n')
                   
                else:      
                    print('Proceso cancelado.')
        else:
            print('Producto no encontrado.')
    except cx_Oracle.DatabaseError as erro:
        print('No fue posible eliminar el producto en la base de datos', erro)
    except Exception as e:
        print('Ocurrio un error inesperado:', e)
    finally:
        cursor.close()
        conexion.close()


def menu_principal():
    exit = False
    """
    Menu principal del sistema para elegir sus diferentes opciones.
    """    
    while not exit:
        limpiar_pantalla()
        print('\n')
        print('=============================================================')
        print('               SISTEMA GESTOR DE INVENTARIOS                 ')
        print('=============================================================\n')

        print('       SELECCIONE LA OPCION DESEADA:\n')
        print('  Agregar un nuevo producto al inventario.==> [1]')
        print('  Consultar productos en existencia.      ==> [2]')
        print('  Actualizar informacion de un producto.  ==> [3]')
        print('  Eliminar un producto del inventario.    ==> [4]')
        print('  Generar un reporte de inventario.       ==> [5]')
        print('               SALIR.                     ==> [6]\n')

        opcion = int(input('Seleccione la opcion deseada: '))        

        if opcion == 1:
            digitar_producto()
        elif opcion == 2:
            consultar_productos()  
        elif opcion == 3:
            actualizar_productos()   
        elif opcion == 4:
            eliminar_productos()                       
        elif opcion == 6:           
            print('Saliendo...')
            exit = True
        else:
            print('Opcion no valida, intente nuevamente.')
        #input('Presione Enter para continuar...')
        
menu_principal()
