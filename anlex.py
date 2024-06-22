from .tablaSimbolos import simbolos

ruta_archivo = 'C:\Facultad Politecnica\Semestre 6\Compiladores\Tarea 1\\fuente.txt'
num_linea = 0

def error(msg):
    print(f"Lin {num_linea}: Error lexico. {msg}")

with open(ruta_archivo, 'r') as archivo:
    c = archivo.read(1)  # lee un solo caracter del archivo
    num_linea = 1
    while c != '':  # mientras haya caracteres para leer
        lexema = ""
        if c == " " or c == "\t":
            pass
        elif c == "\n":
            num_linea += 1
            pass
        elif c.isdigit(): # si es un número
            pass
        elif c == '"': # clave o cadena
            while True:
                lexema = lexema + c
                c = archivo.read(1)
                if c == '"' or c == '': # cierra comilla o termina el archivo
                    lexema = lexema + c
                    break
            if c != '':
                print(simbolos["string"])
                pass # guardar en c el caracter anterior
            else:
                # se termina el archivo sin haber cerrado comillas
                break
        elif c == "t" or c == "T": # true True
            pass
        elif c == "f" or c == "F": # false FALSE
            pass
        elif c == "n" or c == "N": # null NULL
            pass
        elif c == "{":
            pass
        elif c == "[":
            pass
        elif c == "}":
            pass
        elif c == "]":
            pass
        elif c == ",":
            pass
        elif c == ":":
            pass
        c = archivo.read(1)  # Lee el siguiente caracter del archivo
    if c == '':
        print("EOF")


