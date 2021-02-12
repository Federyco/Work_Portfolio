import mysql.connector
from mysql.connector import Error
from tkinter import *
from PIL import ImageTk,Image
import tkinter.font as font
#variables
contador = int(1)
ingreso = int(0)
ingreso_update=int(0)

id_update=int(0)
systemOn = bool(True)


#Visual stuff
screen =Tk()
screen.geometry('1280x651')
screen.title("Pub System 1.0")
screen.iconbitmap("pub_1.0/imgs/wine_glass.ico")
bgImage = PhotoImage(file = "pub_1.0/imgs/background.png")
Label(screen, image = bgImage).place(relwidth =1, relheight=1)
generalFont = font.Font(family='Arial', size=15)   
#falta hacer una función que valide el ingreso por teclado dentro de las Entry
def nuevoProducto(nombre,precio):
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='pruebas'
            )

        if conexion.is_connected():
            insert_producto="INSERT INTO `productos`(`nombre`, `precio`) VALUES ('{0}', '{1}')".format(nombre, precio)
            #creación del cursor, objeto necesario para comunicarse con la base de datos.
            cursor=conexion.cursor()
            cursor.execute(insert_producto)
            conexion.commit() #confirmación de la acción
            print("Producto agregado correctamente")


    except Error as ez:
        print("Error 75, no se pudo agregar el producto ", ez)
    #este bloque siempre se ejecuta
    finally:
        if conexion.is_connected():
            conexion.close()

def listarProductos():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='pruebas'
            )

        if conexion.is_connected():
            #creación del cursor, objeto necesario para comunicarse con la base de datos.
            cursor=conexion.cursor()
            cursor.execute("SELECT * FROM productos")
            resultados=cursor.fetchall()
            for fila in resultados:
                print("ID:" + str(fila[0]), "Producto:" + str(fila[1]), "Precio:" + str(fila[2]))
            #registro=cursor.fetchall() si son muchos registros
            #registro=cursor.fetchone() si es uno solo

    except Error as ez:
        print("Error 46, no se pudo cargar la lista de productos ", ez)
    #este bloque siempre se ejecuta
    finally:
        if conexion.is_connected():
            conexion.close()


def deleteProducto(id):
    
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='pruebas'
            )

        if conexion.is_connected():
            if (validateMe(id) == True):
                delete_producto="DELETE FROM `productos` WHERE id='{0}'".format(id)
                #creación del cursor, objeto necesario para comunicarse con la base de datos.
                cursor=conexion.cursor()
                cursor.execute(delete_producto)
                conexion.commit() #confirmación de la acción
                print("Producto con id " + str(id) + " fue eliminado correctamente")
            else:
                print("No se puede eliminar un producto de ID inexistente")


    except Error as ez:
        print("Error 102, no se pudo eliminar el producto ", ez)
    #este bloque siempre se ejecuta
    finally:
        if conexion.is_connected():
            conexion.close()

def updateNomProducto(id, nombre):
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='pruebas'
            )

        if conexion.is_connected():
            renombrar_producto="UPDATE `productos` SET `nombre`= '{0}' WHERE id='{1}'".format(nombre, id)
            #creación del cursor, objeto necesario para comunicarse con la base de datos.
            cursor=conexion.cursor()
            cursor.execute(renombrar_producto)
            conexion.commit() #confirmación de la acción
            print("Producto con id " + str(id) + " fue renombrado correctamente")


    except Error as ez:
        print("Error 102, no se pudo renombrar el producto ", ez)
    #este bloque siempre se ejecuta
    finally:
        if conexion.is_connected():
            conexion.close()

def updatePrecioProducto(id, precio):
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            db='pruebas'
            )

        if conexion.is_connected():
            nuevo_precio_producto="UPDATE `productos` SET `precio`= '{0}' WHERE id='{1}'".format(precio, id)
            #creación del cursor, objeto necesario para comunicarse con la base de datos.
            cursor=conexion.cursor()
            cursor.execute(nuevo_precio_producto)
            conexion.commit() #confirmación de la acción
            print("Producto con id " + str(id) + " fue actualizado correctamente")


    except Error as ez:
        print("Error 102, no se pudo renombrar el producto ", ez)
    #este bloque siempre se ejecuta
    finally:
        if conexion.is_connected():
            conexion.close()

def busquedaPorId(id):
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='pruebas'
                )

            if conexion.is_connected():
                nuevo_busqueda_producto="SELECT * FROM productos WHERE id='{0}'".format(id)
                #creación del cursor, objeto necesario para comunicarse con la base de datos.
                cursor=conexion.cursor()
                cursor.execute(nuevo_busqueda_producto)
                resultados=cursor.fetchone()
                if resultados is not None:
                    print(resultados[0], resultados[1], resultados[2])
                else:
                    print("El ID buscado no existe")

        except Error as ez:
            print("Error 155, no se pudo cargar la info del producto con id " + str(id), ez)
        #este bloque siempre se ejecuta
        finally:
            if conexion.is_connected():
                conexion.close()
def busquedaPorNombre(texto):
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='pruebas'
                )
            if conexion.is_connected():
                nuevo_busqueda_producto="SELECT * FROM `productos` WHERE nombre LIKE '%{0}%'".format(texto)
                #creación del cursor, objeto necesario para comunicarse con la base de datos.
                cursor=conexion.cursor()
                cursor.execute(nuevo_busqueda_producto)
                resultados=cursor.fetchall()
                if resultados is not None:
                    for fila in resultados:
                        print("ID:" + str(fila[0]), "Producto:" + str(fila[1]), "Precio:" + str(fila[2]))
                else:
                    print("No se encontraron coincidencias")
            

        except Error as ez:
            print("Error 155, no se pudo cargar la info del producto con id " + str(id), ez)
        #este bloque siempre se ejecuta
        finally:
            if conexion.is_connected():
                conexion.close()

def validateMe(id):

        try:
            conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='pruebas'
                )

            if conexion.is_connected():
                nuevo_busqueda_producto="SELECT * FROM productos WHERE id='{0}'".format(id)
                #creación del cursor, objeto necesario para comunicarse con la base de datos.
                cursor=conexion.cursor()
                cursor.execute(nuevo_busqueda_producto)
                resultados=cursor.fetchone()
                if resultados is not None:
                    return True
                else:
                    return False

        except Error as ez:
            print("Error 155, no se pudo cargar la info del producto con id " + str(id), ez)
        #este bloque siempre se ejecuta
        finally:
            if conexion.is_connected():
                conexion.close()


print("Sistema 1.0")
while systemOn == True:
    print("1 - Agregar producto a la base de datos")
    print("2 - Listar productos")
    print("3 - Eliminar un producto")
    print("4 - Actualizar producto")
    print("5 - Busquedas en sistema") # falta ampliar para buqueda por precios y nombres y que el menú sea "busquedas"
    print("6 - Salir")
    ingreso=input("Su elección: ")
    while not (ingreso.isdigit()):
        print("Sólo se permiten ingresos numéricos")
        ingreso=input("Su elección: ")
    if int(ingreso) == int(1):
        print("Insertando un nuevo producto en al base de datos")
        nombre_producto=input("Indique el nombre del producto: ")
        while (nombre_producto.isdigit()):
            print("Sólo se permiten ingresos de texto o símbolos")
            nombre_producto=input("Indique el nombre del producto: ")
        precio_producto=input("Indique el precio del producto " + str(nombre_producto) + ": ")
        while (precio_producto.isdecimal()):
            print("Solo se permiten valores numéricos decimales EJ. 0.0")
            precio_producto=input("Indique el precio del producto " + str(nombre_producto) + ": ")
        nuevoProducto(nombre_producto, precio_producto)
    if int(ingreso) == int(2):
        print("Listado actual de productos")
        listarProductos()
    if int(ingreso) == int(3):
        id_producto = input("Ingrese el ID del producto a eliminar: ")
        while not (id_producto.isdigit()):
            print("Sólo se permiten ingresos numéricos")
            id_producto = input("Ingrese el ID del producto a eliminar: ")
        deleteProducto(id_producto)
    if int(ingreso) == int(4):
        print("Actualizar productos")
        print("Para realizar esta actualización, se requiere el ID del producto")
        id_update=input("Ingrese por favor, el id del producto: ")
        while not (id_update.isdigit()):
            print("Sólo se permiten ingresos numéricos")
            id_update=input("Ingrese por favor, el id del producto: ")
        print("1 - Para actualizar el nombre de un producto")
        print("2 - Para actualizar el precio de un producto")
        print("3 - Salir del Sistema")
        ingreso_update=input("Su Elección: ")
        while not (ingreso_update.isdigit()):
            print("Sólo se permiten ingresos numéricos")
            ingreso_update=input("Su Elección: ")
        if int(ingreso_update) == int(1):
            update_nombre=str(" ")
            update_nombre=input("Ingrese el nuevo nombre del producto deseado: ")
            while (update_nombre.isdigit()):
                print("Sólo se permiten ingresos de texto o símbolos")
                update_nombre=input("Ingrese el nuevo nombre del producto deseado: ")
            updateNomProducto(id_update, update_nombre)
        if int(ingreso_update) == int(2):
            update_precio=float(0.0)
            update_precio=input("Ingrese el nuevo precio del producto deseado: ")
            while (update_precio.isdecimal()):
                print("Solo se permiten valores numéricos decimales EJ. 0.0")
                update_precio=input("Ingrese el nuevo precio del producto deseado: ")  
            updatePrecioProducto(id_update, update_precio)
        if int(ingreso_update) == int(3):
            print("Saliendo del Sistema 1.0")
            systemOn = False
    # busquedas en sistema
    if int(ingreso) == int(5):
        ingreso_busqueda=int(0)
        print("Busquedas en sistema 1.0")
        print("1 - Busqueda por ID")
        print("2 - Busqueda por nombre")
        print("3 - Busqueda por precio")
        print("4 - Salir")
        ingreso_busqueda=input("Su elección: ")
        while not (ingreso_busqueda.isdigit):
            print("Sólo se permiten ingresos numéricos")
            ingreso_busqueda=input("Su elección: ")
        if(int(ingreso_busqueda) == int(1)):
            id_a_buscar=int(0)
            id_a_buscar=input("Ingrese el Id de producto que desea buscar: ")
            while not (id_a_buscar.isdigit()):
                print("Sólo se permiten ingresos numéricos")
                id_a_buscar=input("Ingrese el Id de producto que desea buscar: ")
            busquedaPorId(id_a_buscar)
        if int(ingreso_busqueda) == int(2):
            nombre_a_buscar=str(" ")
            nombre_a_buscar=input("Ingrese el nombre del producto que desea buscar: ")
            while not(nombre_a_buscar.isdigit):
                print("Sólo se permiten ingresos de texto o símbolos")
                nombre_a_buscar=input("Ingrese el nombre del producto que desea buscar: ")
            busquedaPorNombre(nombre_a_buscar)
        
        if int(ingreso_busqueda) == int(4):
            print("Saliendo del Sistema 1.0")
            systemOn = False
    if int(ingreso) == int(6):
        print("Saliendo del Sistema 1.0")
        systemOn = False

#programa base
screen.mainloop()