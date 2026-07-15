"""Sistema para administrar un inventario de libros"""


def mostrarMenu():
    libreria = []
    while True:
        print("------------------------------------------")
        print("LIBRERIA EL SABER")
        print("1.- Agregar libro")
        print("2.- Mostrar un libro")
        print("3.- Eliminar libro")
        print("4.- Listar inventario")
        print("5.- Valorizar inventario")
        print("6.- Salir")
        while True:
            try:
                opc = int(input("Ingrese la opcion que desea: "))
                if validarOpc(opc):
                    break
            except ValueError:
                print("Formato no valido")
                
        if opc == 1:
            agregarLibro(libreria)
        elif opc == 2:
            mostrarLibro(libreria)
        elif opc == 3:
            eliminarLibro(libreria)
        elif opc == 4:
            print()
        elif opc == 5:
            print()
        elif opc == 6:
            print("Fin del programa")
            break

def validarCodigo(codigo):
    if len(codigo) == 7 and codigo[0].isalpha() and codigo[1].isalpha() and codigo[2].isalnum() and codigo[3].isalnum() and codigo[4].isalnum() and codigo[5].isnumeric() and codigo[6].isnumeric():
        return True
    else:
        return False

def validarAño(año):
    return año > 1450 and año <= 2026

def validarPrecio(precio):
    return precio>0

def validarTitulo(titulo):
    return titulo.strip()!=""

def validarOpc(opc):
    return opc > 0 and opc <= 6

def agregarLibro(libreria):
    while True:
        codigo = input("Ingrese el codigo del libro: ")
        if validarCodigo(codigo):
            break
    while True:
        titulo = input("Ingrese titulo del libro: ")
        if validarTitulo(titulo):
            break
    while True:
        año = int(input("Ingrese el año de publicación: "))
        if validarAño(año):
            break
    while True:
        precio = int(input("Ingrese el precio del libro: "))
        if validarPrecio(precio):
            break
    dic = {"codigo":codigo,
           "titulo":titulo,
           "año":año,
           "precio":precio}
    libreria.append(dic)
        

def buscarLibro(titulo,libreria):
    pos = -1
    for i in range(len(libreria)):
        if libreria[i]['titulo']==titulo:
            pos = i
            break
    return pos

def mostrarLibro(libreria):
    titulo = input("Ingrese el titulo del libro que desea visualizar: ")
    ubicacion = buscarLibro(titulo,libreria)
    print("------------------------------------------")
    if ubicacion > -1:
        print(f"Titulo: {libreria[ubicacion]['titulo']}")
        print(f"Codigo: {libreria[ubicacion]['codigo']}")
        print(f"Año: {libreria[ubicacion]['año']}")
        print(f"Precio: {libreria[ubicacion]['precio']}")
    else:
        print("Libro no encontrado.")
    
def eliminarLibro(libreria):
    titulo = input("Ingrese el titulo del libro que desea eliminar: ")
    ubicacion = buscarLibro(titulo,libreria)
    if ubicacion > -1:
        print("-------------------------------------")
        print("Libro eliminado con exito")
        libreria.pop(ubicacion)
    else:
        print("No valido, libro no encontrado.")


mostrarMenu()

