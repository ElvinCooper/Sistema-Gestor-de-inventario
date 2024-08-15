import cx_Oracle
import os, sys


def limpiar_input():
    sys.stdout.write('\r')  # mueve el cursor al principio de la linea

    sys.stdout.write(' ' * 80) # limpiar la linea sobreescribiendo con espacios hasta 80 carcteres

    sys.stdout.write('\r') # mueve el cursor al principio de la linea nuevamente
    sys.stdout.flush()


# Insercion de productos
def digitar_producto():
    print('=============================================================')
    print('               AGREGAR NUEVO PRODUCTO                        ')
    print('=============================================================\n')    

    codigo    = int(input('Ingrese el código del producto: '))
    nombre    = input('Ingrese el nombre del producto:     ')
    categoria = input('Ingrese la categoria del producto: ')
    cantidad  = int(input('Ingrese la cantidad en stock: '  ))
    precio    = int(input('Ingrese el precio unitario: '    ))

    try:
        conexion = cx_Oracle.connect(
            user = 'TRAIN7',
            password = 'TRAIN7',
            dsn = 'SID_CR1'
        )
    except cx_Oracle.DatabaseError as err:
        print('No fue posible establecer la conexion', err)    
    # else:
    #     print('La conexion fue exitosa', conexion.version)    

    cursor = conexion.cursor()    
    query = f"INSERT INTO INVENTARIO VALUES ({codigo}, '{nombre}', '{categoria}' , {cantidad}, {precio})\n"
    cursor.execute(query)

    conexion.commit()

    # cerrar el comando y la conexion a la base de datos
    cursor.close()
    conexion.close()

    print('Producto agregado exitosamente al inventario\n')

    opcion = input('Presione 0 para regresar al menu principal: ') 


# Consultar productos
def consultar_productos():
    print('=============================================================')
    print('               CONSULTA DE PRODUCTOS                         ')
    print('=============================================================\n') 

    id_codigo = int(input('Digite el codigo del producto: '))
    limpiar_input()

    try:
        conexion = cx_Oracle.connect(
            user = 'TRAIN7',
            password = 'TRAIN7',
            dsn = 'SID_CR1'
        )
    except cx_Oracle.DatabaseError as err:
        print('No fue posible establecer la conexion', err)   
        return     

    cursor = conexion.cursor()    
    query = f"SELECT * FROM INVENTARIO WHERE ID_PRODUCTO = {id_codigo}"
    cursor.execute(query)
    resultado = cursor.fetchall()

    for row in resultado:
        codigo     = row[0]
        descripcon = row[1]
        categoria   = row[2]
        cantidad  = row[3]
        precio     = row[4]

        print(f'Codigo: {codigo}\nDescripcion: {descripcon}\nCantidad: {cantidad}\nCategoria: {categoria}\nPrecio: {precio}\n')        

    # cerrar el comando y la conexion a la base de datos
    cursor.close()
    conexion.close()        

def limpiar_pantalla():
    # Verifica si el sistema operativo es Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

         
# Pantalla de Bienvenida
def menu_principal():
    while True:
        print('=============================================================')
        print('               SISTEMA GESTOR DE INVENTARIOS                 ')
        print('=============================================================\n')

        print('Por favor, seleccione una opcion:\n')
        print('1. Agregar un nuevo producto al inventario')
        print('2. Consultar productos en existencia')
        print('3. Actualizar información de un producto')
        print('4. Eliminar un producto del inventario')
        print('5. Generar un reporte de inventario')
        print('6. Salir\n')

        opcion = int(input('Seleccione la opcion deseada: '))
        limpiar_input()

        if opcion == 1:
            digitar_producto()
        elif opcion == 2:
            consultar_productos()    
        elif opcion == 0:
            print('Saliendo...')            
            break
        else:
            print('Opcion no valida, intente nuevamente.')
            limpiar_input()
menu_principal()            
