import cx_Oracle

class Articulos:

    def abrir(self):
        conexion = cx_Oracle.connect(dsn="localhost/xe",
                                              user="PYTHONTKINTER",
                                              password="1qazxsw2"
                                              )
        return conexion

    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute= ("insert into articulos values (%s, %s)", datos)
        cursor.fetchall()
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute = ("select descripcion, precio from articulos where codigo=%s", datos)
        cursor.fetchall()
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select codigo, descripcion, precio from articulos"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def baja(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="delete from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount # retornamos la cantidad de filas borradas

    def modificacion(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="update articulos set descripcion=%s, precio=%s where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount # retornamos la cantidad de filas modificadas