from itertools import product, chain, combinations

def p1():
    print("Indica si cada declaración es verdadera o falsa\n")

    # El conjunto {4, 0, 3, 0} es igual a {4, 4, 0, 3} ?
    print("El conjunto {4, 0, 3, 0} == {4, 4, 0, 3}?")
    if {4, 0, 3, 0} == {4, 4, 0, 3}:
        print("Verdadero", {4, 0, 3, 0}, {4, 4, 0, 3})
    else:
        print("Falso")

    # El conjunto {4} es subconjunto propio de {0, 3, 4} ?
    print("\nEl conjunto {4} es subconjunto propio de {0, 3, 4}?")
    if {4} < {0, 3, 4}:  # < indica subconjunto propio
        print("Verdadero")
    else:
        print("Falso")

    # El conjunto {0, 3, 4} es subconjunto propio de {3} ?
    print("\nEl conjunto {0, 3, 4} es subconjunto propio de {3}?")
    if {0, 3, 4} < {3}:
        print("Verdadero")
    else:
        print("Falso")

    # El conjunto {0, 3, 4} es subconjunto propio de {0, 3, 4} ?
    print("\nEl conjunto {0, 3, 4} es subconjunto propio de {0, 3, 4}?")
    if {0, 3, 4} < {0, 3, 4}:
        print("Verdadero")
    else:
        print("Falso, no es un subconjunto propio")

    # El conjunto vacío es subconjunto propio de {0, 3, 4} ?
    print("\nEl conjunto vacío es subconjunto propio de {0, 3, 4}?")
    if set() < {0, 3, 4}:  # conjunto vacío es subconjunto propio de cualquier conjunto no vacío
        print("Verdadero")
    else:
        print("Falso")

def p2():
    conjunto = {0, 3, 4, 7}
    print("\nEl conjunto potencia P({0, 3, 4, 7}) es el conjunto de todos los subconjuntos de {0, 3, 4, 7}:")

    # Generar todos los subconjuntos usando itertools
    potencia = list(map(set, chain.from_iterable(combinations(conjunto, r) for r in range(len(conjunto)+1))))
    
    print(potencia)

def p3():
    # Crear conjuntos correctamente usando llaves o set() con iterable
    A = {1, 2, 3, 4}
    B = {2, 3, 5, 8}

    # operaciones de conjuntos
    print("\nOperaciones de conjuntos:")
    print("A ∪ B =", A.union(B))
    print("A ∩ B =", A.intersection(B))
    print("A - B =", A.difference(B))
    # Producto Cartesiano
    print("A × B =", set(product(A, B)))


# Ejecutar funciones
print("Ejercicio 1:")
p1()
print("\nEjercicio 2:")
p2()
print("\nEjercicio 3:")
p3()