"""Sistema para administrar un inventario de libros"""


def mostrarMenu():
    libereria = []
    print("------------------------------")
    print("LIBRERIA EL SABER")
    print("1.- Agregar libro")
    print("2.- Mostrar un libro")
    print("3.- Eliminar libro")
    print("4.- Listar inventario")
    print("5.- Valorizar inventario")
    print("6.- Salir")

    if opc == 1:
        print()
    elif opc == 2:
        print()
    elif opc == 3:
        print()
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
        precio = int(input("Ingrese el precio del libro"))
        if validarPrecio(precio):
            break
    dic = {"codigo":codigo,
           "titulo":titulo,
           "año":año,
           "precio":precio}
    libreria.append(dic)
        
     
    
        


