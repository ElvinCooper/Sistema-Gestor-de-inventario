import cx_Oracle


try:
    conexion = cx_Oracle.connect(
        user = 'TRAIN7',
        password = 'TRAIN7',
        dsn = 'SID_CR1'
    )
except cx_Oracle.DatabaseError as err:
    print('No fue posible establecer la conexion', err)    
else:
    print('La conexion fue exitosa', conexion.version)    

cursor = conexion.cursor()    
query = 'CREATE TABLE INVENTARIO (ID_PRODUCTO NUMBER(4), DESCRIPCION_PRODUCTO VARCHAR2(60), CATEGORIA VARCHAR2(50), CANTIDAD NUMBER, PRECIO NUMBER)'
cursor.execute(query)

conexion.close()

