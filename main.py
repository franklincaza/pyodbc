import pyodbc

def conexionBD():
    """
    datos para conectar la base datos con pyodbc los datos ejemplo
        server : 'tcp:myserver.database.windows.net'
        database : 'mydb'
        username : 'myusername'
        password : 'mypassword'
    """
    try:
        server = str(config ("server"))
        database = str(config ("database"))
        username = str(config ("username"))
        password = str(config ("pass"))


        connection =pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server +
            ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)


        logging.info("Conectando ala base datos con exito")
        return connection
    except:
         logging.error("Error en conectar , la base de datos ")
         print("Error en conectar , la base de datos ")


def Select_datos_sql(query):
    """
    funcion para leer tabla  valores en SQLserve:
    debe consultar el config.xlsx que esta en el archivo de excel en la carpeta
    data por ejemplo :
    ____________________________________________________________________________
    Select_datos_sql(NOMINA_COBRO_TRAB_VCTO )
    ____________________________________________________________________________
    """
    try:
        connection = conexionBD()
        cursor = connection.cursor()
        Dt= cursor.execute(query)
        return Dt
        cursor.close()
    except:
        logging.error("Error en el select revisar la funcion def Select_datos_sql(query) ")
