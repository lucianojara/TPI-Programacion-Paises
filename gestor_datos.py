import csv

def cargar_datos_csv(ruta_archivo):
    """
    Lee el archivo CSV y devuelve una lista de diccionarios con los datos de los países.
    Controla errores de archivo inexistente o formato inválido en las filas.
    """
    lista_paises = []

    try:
        with open(ruta_archivo, mode="r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)

            columnas_requeridas = ["nombre", "poblacion", "superficie", "continente"]
            if not lector.fieldnames or not all(col in lector.fieldnames for col in columnas_requeridas):
                print("[ERROR] El archivo CSV no tiene las columnas requeridas.")
                return lista_paises

            for numero_fila, fila in enumerate(lector, start=2):
                try:
                    nombre = fila["nombre"].strip()
                    continente = fila["continente"].strip()
                    poblacion = int(fila["poblacion"].strip())
                    superficie = int(fila["superficie"].strip())

                    if nombre == "" or continente == "" or poblacion <= 0 or superficie <= 0:
                        print(f"[ADVERTENCIA] Fila {numero_fila} omitida por datos vacíos o inválidos.")
                        continue

                    pais = {
                        "nombre": nombre,
                        "poblacion": poblacion,
                        "superficie": superficie,
                        "continente": continente
                    }
                    lista_paises.append(pais)

                except (ValueError, TypeError, AttributeError):
                    print(f"[ADVERTENCIA] Fila {numero_fila} omitida por error de formato.")

        print(f"[ÉXITO] Se cargaron {len(lista_paises)} países desde '{ruta_archivo}'.")

    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo '{ruta_archivo}'. Se iniciará con una lista vacía.")
    except Exception as error:
        print(f"[ERROR] No se pudo leer el archivo: {error}")

    return lista_paises


def guardar_datos_csv(ruta_archivo, lista_paises):
    """
    Guarda la lista de diccionarios actualizada en el archivo CSV.
    """
    try:
        with open(ruta_archivo, mode="w", encoding="utf-8", newline="") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(lista_paises)
    except Exception as error:
        print(f"[ERROR] No se pudieron guardar los cambios en el archivo: {error}")


def pedir_texto_obligatorio(mensaje):
    """
    Solicita un texto por consola y valida estrictamente que no esté vacío.
    """
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("[ERROR] Este campo no puede quedar vacío. Intente nuevamente.")


def pedir_entero_positivo(mensaje):
    """
    Solicita un número entero mayor a 0 y controla errores de ingreso.
    """
    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            print("[ERROR] El campo no puede quedar vacío.")
            continue

        try:
            numero = int(entrada)
            if numero > 0:
                return numero
            print("[ERROR] El número debe ser mayor a cero.")
        except ValueError:
            print("[ERROR] Entrada inválida. Ingrese un número entero sin puntos ni comas.")


def obtener_indice_pais(lista_paises, nombre_buscado):
    """
    Busca un país por nombre exacto (sin importar mayúsculas) y devuelve su índice en la lista.
    Si no existe, devuelve -1.
    """
    for indice, pais in enumerate(lista_paises):
        if pais["nombre"].lower() == nombre_buscado.lower():
            return indice
    return -1


def agregar_pais(lista_paises, ruta_archivo):
    """
    Agrega un nuevo diccionario de país a la lista principal y actualiza el CSV.
    """
    print("\n--- AGREGAR NUEVO PAÍS ---")
    nombre = pedir_texto_obligatorio("Ingrese el nombre del país: ")

    if obtener_indice_pais(lista_paises, nombre) != -1:
        print(f"[ERROR] El país '{nombre}' ya está registrado en el sistema.")
        return

    poblacion = pedir_entero_positivo("Ingrese la población: ")
    superficie = pedir_entero_positivo("Ingrese la superficie en km²: ")
    continente = pedir_texto_obligatorio("Ingrese el continente: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    lista_paises.append(nuevo_pais)
    guardar_datos_csv(ruta_archivo, lista_paises)
    print(f"[ÉXITO] País '{nombre}' agregado correctamente.")


def actualizar_pais(lista_paises, ruta_archivo):
    """
    Actualiza la población y superficie de un país existente en la lista y en el CSV.
    """
    print("\n--- ACTUALIZAR DATOS DE UN PAÍS ---")
    if len(lista_paises) == 0:
        print("[AVISO] No hay países cargados en el sistema.")
        return

    nombre = pedir_texto_obligatorio("Ingrese el nombre exacto del país a actualizar: ")
    indice = obtener_indice_pais(lista_paises, nombre)

    if indice == -1:
        print(f"[ERROR] No se encontró el país '{nombre}'.")
        return

    pais_actual = lista_paises[indice]
    print(f"Datos actuales de {pais_actual['nombre']} -> Población: {pais_actual['poblacion']:,} | Superficie: {pais_actual['superficie']:,} km²")

    nueva_poblacion = pedir_entero_positivo("Ingrese la nueva población: ")
    nueva_superficie = pedir_entero_positivo("Ingrese la nueva superficie en km²: ")

    lista_paises[indice]["poblacion"] = nueva_poblacion
    lista_paises[indice]["superficie"] = nueva_superficie
    guardar_datos_csv(ruta_archivo, lista_paises)
    print(f"[ÉXITO] Datos de '{pais_actual['nombre']}' actualizados correctamente.")


def buscar_pais_por_nombre(lista_paises):
    """
    Busca países por coincidencia exacta o parcial y los muestra en consola.
    """
    print("\n--- BUSCAR PAÍS POR NOMBRE ---")
    if len(lista_paises) == 0:
        print("[AVISO] No hay países cargados en el sistema.")
        return

    termino = pedir_texto_obligatorio("Ingrese el nombre o parte del nombre a buscar: ").lower()
    resultados = []

    for pais in lista_paises:
        if termino in pais["nombre"].lower():
            resultados.append(pais)

    if len(resultados) == 0:
        print(f"[AVISO] No se encontraron países que coincidan con '{termino}'.")
    else:
        print(f"\n[ÉXITO] Se encontraron {len(resultados)} resultado(s):")
        for p in resultados:
            print(f" - {p['nombre']} | Continente: {p['continente']} | Población: {p['poblacion']:,} | Superficie: {p['superficie']:,} km²")
