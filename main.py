import gestor_datos
import consultas

ARCHIVO_CSV = "paises.csv"

def mostrar_menu():
    print("")
    print("   SISTEMA DE GESTIÓN DE DATOS DE PAÍSES")
    print("")
    print("1. Agregar un país")
    print("2. Actualizar población y superficie de un país")
    print("3. Buscar país por nombre")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("0. Salir")
    print("")

def main():
    paises = gestor_datos.cargar_datos_csv(ARCHIVO_CSV)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion (0-6): ").strip()

        match opcion:
            case "1":
                gestor_datos.agregar_pais(paises, ARCHIVO_CSV)
            case "2":
                gestor_datos.actualizar_pais(paises, ARCHIVO_CSV)
            case "3":
                gestor_datos.buscar_pais_por_nombre(paises)
            case "4":
                consultas.menu_filtrar(paises)
            case "5":
                consultas.menu_ordenar(paises)
            case "6":
                consultas.mostrar_estadisticas(paises)
            case "0":
                print("\n Saliendo del sistema. ¡Hasta luego!")
                break
            case _:
                print("\n Opción inválida. Ingrese un número del 0 al 6.")

if __name__ == "__main__":
    main()
