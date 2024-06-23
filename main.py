import anlex
from ansic import AnalizadorSintactico

def main():
    ruta_archivo = 'fuente.txt'
    ruta_salida = 'output.txt'

    try:
        resultado, valido = anlex.analizar_archivo(ruta_archivo)
        anlex.guardar_resultado(resultado, ruta_salida)
        if not  valido:
            print("Error léxico. Revise el archivo {}".format(ruta_archivo))
        ansic = AnalizadorSintactico(resultado)
        ansic.analizar_archivo(resultado)
    except IOError as e:
        print(f"Error al abrir el archivo: {e}")
    except Exception as e:
        print(f"Se produjo un error: {e}")

if __name__ == "__main__":
    main()