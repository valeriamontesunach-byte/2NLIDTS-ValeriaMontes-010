class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Función Agregar elementos a la lista
def agregarNodo(cabeza, valor):
    nuevoNodo = Nodo(valor) # Creando el apuntador hacia el nuevo nodo

    if cabeza is None:
        return nuevoNodo
    else:
        actual = cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevoNodo
        return cabeza

def imprimirlista(cabeza):
    actual = cabeza
    while actual is not None:
        print(actual.dato, end=" ")
        actual = actual.siguiente
    print()

def borradorLista(cabeza):
    while cabeza is not None:
        siguiente = cabeza.siguiente
        del cabeza
        cabeza = siguiente
        print("Elemento borrado ", end="")
    print()

def main():
    cabeza = None # Declaramos un puntero de memoria nulo
    
    try:
        tamanoLista = int(input("Ingrese la cantidad de elementos que desea agregar a la lista: "))
    except ValueError:
        print("Cantidad de elementos no valida")
        return 1

    if tamanoLista <= 0:
        print("Cantidad de elementos no valida")
        return 1

    for i in range(tamanoLista):
        valor = int(input(f"Ingresedato {i + 1}: "))
        # Invocamos nuestra funcion de agregar Nodo
        cabeza = agregarNodo(cabeza, valor)

    print("Imprimiendo Lista de numeros")
    imprimirlista(cabeza)
    
    borradorLista(cabeza)
    return 0

if __name__ == "__main__":
    main()
