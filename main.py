import anlex

def main():
    ruta_archivo = 'fuente.txt'
    ruta_salida = 'output.txt'

    resultado = anlex.analizar_archivo(ruta_archivo)
    anlex.guardar_resultado(resultado, ruta_salida)

if __name__ == "__main__":
    main()