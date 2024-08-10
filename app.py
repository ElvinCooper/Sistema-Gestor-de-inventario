import cx_Oracle
import os


# Pantalla de Bienvenida
def menu_principal():
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

    


menu_principal()


# Insercion de productos
def digitar_producto():
    print('=============================================================')
    print('               AGREGAR NUEVO PRODUCTO                        ')
    print('=============================================================\n')    

    codigo   = int(input('Ingrese el código del producto: '))
    nombre   = input('Ingrese el nombre del producto:     ')
    categoria = input('Ingrese la categoria del producto: ')
    cantidad = int(input('Ingrese la cantidad en stock: '  ))
    precio   = int(input('Ingrese el precio unitario: '    ))

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
    #print('Presione cualquier tecla para regresar al menu principal')
    if opcion == 0:
        menu_principal()    



def consultar_productos():
    print('=============================================================')
    print('               CONSULTA DE PRODUCTOS                         ')
    print('=============================================================\n') 

    id_codigo = int(input('Digite el codigo del producto: '))


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
    query = f"SELECT * FROM INVENTARIO WHERE ID_PRODUCTO = {id_codigo}"
    cursor.execute(query)
    resultado = cursor.fetchall()

    for row in resultado:
        codigo     = row[0]
        descripcon = row[1]
        cantidad   = row[2]
        categoria  = row[3]
        precio     = row[4]

        print(f'Codigo: {codigo}\nDescripcion: {descripcon}\nCantidad: {cantidad}\nCategoria: {categoria}\nPrecio: {precio}\n')        

    # cerrar el comando y la conexion a la base de datos
    cursor.close()
    conexion.close()        

    while True:
        salida = input('Presione 0 para volver al menu principal: ')
        if salida == 0:
            break
    menu_principal()
    # opcion = input('Presione 0 para regresar al menu principal: ') 
    
    # if opcion == 0:
    #     menu_principal()


def limpiar_pantalla():
    # Verifica si el sistema operativo es Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


opcion = int(input('Opcion deseada: '))
if opcion == 1:
    #limpiar_pantalla()
    digitar_producto()
elif opcion == 2:
    #limpiar_pantalla()    
    consultar_productos()
elif opcion == 6:
    exit 
         

