from tablaSimbolos import simbolos
EOF = ""

def analizar_archivo(lexemas):
    token_actual = None
    posicion_actual = 0
    def get_token():
        nonlocal token_actual
        nonlocal posicion_actual
        if posicion_actual < len(lexemas):
            token_actual = lexemas[posicion_actual]
            posicion_actual += 1
        else:
            return None
    # Inicia el analisis sintactico
    get_token()
    conjunto_sgte = [EOF]
    json(conjunto_sgte)

def json(synchset):
    conjunto_prim = []
    check_input(conjunto_prim, synchset)
    pass

def element(synchset):
    pass

def array(synchset):
    pass

def element_list(synchset):
    pass

def element_list_aux(synchset):
    pass

def object(synchset):
    pass

def attribute_list(synchset):
    pass

def attribute_list_aux(synchset):
    pass

def attribute(synchset):
    pass

def attribute_name(synchset):
    pass

def attribute_value(synchset):
    pass

# Funciones para Panic Mode
def check_input(firsts, follows):
    pass

def scanto(synchset):
    pass