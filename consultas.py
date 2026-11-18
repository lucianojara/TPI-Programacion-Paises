# ==========================================
# FILTROS
# ==========================================

def filtrar_por_continente(paises):
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    continente_buscado = input("Ingrese el continente: ").strip().lower()
    resultado = []

    for pais in paises:
        if pais["continente"].strip().lower() == continente_buscado:
            resultado.append(pais)

    if len(resultado) > 0:
        print("\nPaises encontrados:")
        for pais in resultado:
            print(f"- {pais['nombre']}: {pais['poblacion']} habitantes - {pais['superficie']} km2")
    else:
        print("No se encontraron paises en ese continente.")


def filtrar_por_poblacion(paises):
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    while True:
        minimo = input("Ingrese la poblacion minima: ").strip()
        maximo = input("Ingrese la poblacion maxima: ").strip()

        if not minimo.isdigit() or not maximo.isdigit():
            print("ERROR. Ingrese solamente numeros.")
        else:
            minimo = int(minimo)
            maximo = int(maximo)

            if minimo > maximo:
                print("La poblacion minima no puede ser mayor a la maxima.")
            else:
                break

    resultado = []

    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            resultado.append(pais)

    if len(resultado) > 0:
        print("\nPaises encontrados:")
        for pais in resultado:
            print(f"- {pais['nombre']}: {pais['poblacion']} habitantes")
    else:
        print("No se encontraron paises dentro del rango ingresado.")


def filtrar_por_superficie(paises):
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    while True:
        minimo = input("Ingrese la superficie minima: ").strip()
        maximo = input("Ingrese la superficie maxima: ").strip()

        if not minimo.isdigit() or not maximo.isdigit():
            print("ERROR. Ingrese solamente numeros.")
        else:
            minimo = int(minimo)
            maximo = int(maximo)

            if minimo > maximo:
                print("La superficie minima no puede ser mayor a la maxima.")
            else:
                break

    resultado = []

    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultado.append(pais)

    if len(resultado) > 0:
        print("\nPaises encontrados:")
        for pais in resultado:
            print(f"- {pais['nombre']}: {pais['superficie']} km2")
    else:
        print("No se encontraron paises dentro del rango ingresado.")


def menu_filtrar(paises):
    while True:
        print("\n--- SUBMENÚ DE FILTROS ---")
        print("1. Filtrar por continente")
        print("2. Filtrar por rango de población")
        print("3. Filtrar por rango de superficie")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                filtrar_por_continente(paises)
            case "2":
                filtrar_por_poblacion(paises)
            case "3":
                filtrar_por_superficie(paises)
            case "0":
                break
            case _:
                print("Opción inválida.")


# ==========================================
# ORDENAMIENTOS
# ==========================================

def ordenar_por_nombre(paises):
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    orden = input("Ingrese 1 para A-Z o 2 para Z-A: ").strip()

    while orden != "1" and orden != "2":
        print("Opcion invalida.")
        orden = input("Ingrese 1 para A-Z o 2 para Z-A: ").strip()

    for i in range(len(paises) - 1):
        for j in range(len(paises) - 1 - i):
            nombre_actual = paises[j]["nombre"].lower()
            nombre_siguiente = paises[j + 1]["nombre"].lower()

            if orden == "1" and nombre_actual > nombre_siguiente:
                auxiliar = paises[j]
                paises[j] = paises[j + 1]
                paises[j + 1] = auxiliar
            elif orden == "2" and nombre_actual < nombre_siguiente:
                auxiliar = paises[j]
                paises[j] = paises[j + 1]
                paises[j + 1] = auxiliar

    print("\nPaises ordenados:")
    for pais in paises:
        print(f"- {pais['nombre']}")


def ordenar_por_poblacion(paises):
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    orden = input("Ingrese 1 para menor a mayor o 2 para mayor a menor: ").strip()

    while orden != "1" and orden != "2":
        print("Opcion invalida.")
        orden = input("Ingrese 1 para menor a mayor o 2 para mayor a menor: ").strip()

    for i in range(len(paises) - 1):
        for j in range(len(paises) - 1 - i):
            poblacion_actual = paises[j]["poblacion"]
            poblacion_siguiente = paises[j + 1]["poblacion"]

            if orden == "1" and poblacion_actual > poblacion_siguiente:
                auxiliar = paises[j]
                paises[j] = paises[j + 1]
                paises[j + 1] = auxiliar
            elif orden == "2" and poblacion_actual < poblacion_siguiente:
                auxiliar = paises[j]
                paises[j] = paises[j + 1]
                paises[j + 1] = auxiliar

    print("\nPaises ordenados:")
    for pais in paises:
        print(f"- {pais['nombre']}: {pais['poblacion']} habitantes")


def ordenar_por_superficie(paises):
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    orden = input("Ingrese 1 para menor a mayor o 2 para mayor a menor: ").strip()

    while orden != "1" and orden != "2":
        print("Opcion invalida.")
        orden = input("Ingrese 1 para menor a mayor o 2 para mayor a menor: ").strip()

    for i in range(len(paises) - 1):
        for j in range(len(paises) - 1 - i):
            superficie_actual = paises[j]["superficie"]
            superficie_siguiente = paises[j + 1]["superficie"]

            if orden == "1" and superficie_actual > superficie_siguiente:
                auxiliar = paises[j]
                paises[j] = paises[j + 1]
                paises[j + 1] = auxiliar
            elif orden == "2" and superficie_actual < superficie_siguiente:
                auxiliar = paises[j]
                paises[j] = paises[j + 1]
                paises[j + 1] = auxiliar

    print("\nPaises ordenados:")
    for pais in paises:
        print(f"- {pais['nombre']}: {pais['superficie']} km2")


def menu_ordenar(paises):
    while True:
        print("\n--- SUBMENÚ DE ORDENAMIENTO ---")
        print("1. Ordenar por nombre")
        print("2. Ordenar por población")
        print("3. Ordenar por superficie")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                ordenar_por_nombre(paises)
            case "2":
                ordenar_por_poblacion(paises)
            case "3":
                ordenar_por_superficie(paises)
            case "0":
                break
            case _:
                print("Opción inválida.")


# ==========================================
# ESTADISTICAS
# ==========================================

def pais_mayor_poblacion(paises):
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    mayor = paises[0]
    for pais in paises:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais

    print(f"El pais con mayor poblacion es {mayor['nombre']} con {mayor['poblacion']} habitantes.")


def pais_menor_poblacion(paises):
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    menor = paises[0]
    for pais in paises:
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

    print(f"El pais con menor poblacion es {menor['nombre']} con {menor['poblacion']} habitantes.")


def promedio_poblacion(paises):
    if len(paises) == 0:
        print("No hay paises para calcular el promedio.")
        return

    suma = 0
    for pais in paises:
        suma += pais["poblacion"]

    promedio = suma / len(paises)
    print(f"Promedio de poblacion general: {promedio:.2f} habitantes")


def promedio_superficie(paises):
    if len(paises) == 0:
        print("No hay paises para calcular el promedio.")
        return

    suma = 0
    for pais in paises:
        suma += pais["superficie"]

    promedio = suma / len(paises)
    print(f"Promedio de superficie general: {promedio:.2f} km2")


def paises_por_continente(paises):
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    america = 0
    asia = 0
    europa = 0
    oceania = 0
    africa = 0

    for pais in paises:
        continente = pais["continente"].strip().lower()
        if continente in ("america", "américa"):
            america += 1
        elif continente == "asia":
            asia += 1
        elif continente == "europa":
            europa += 1
        elif continente in ("oceania", "oceanía"):
            oceania += 1
        elif continente in ("africa", "áfrica"):
            africa += 1

    print(f"""
Cantidad de paises por continente:
- America = {america}
- Asia = {asia}
- Europa = {europa}
- Oceania = {oceania}
- Africa = {africa}""")


def mostrar_estadisticas(paises):
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    print("\n--- ESTADÍSTICAS GENERALES ---")
    pais_mayor_poblacion(paises)
    pais_menor_poblacion(paises)
    promedio_poblacion(paises)
    promedio_superficie(paises)
    paises_por_continente(paises)
