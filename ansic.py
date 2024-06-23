from tablaSimbolos import simbolos
EOF = ""

class AnalizadorSintactico:
    def __init__(self, lexemas):
        self.lexemas = lexemas
        self.posicion_actual = 0
        self.token_actual = None
        self.get_token()

    def get_token(self):
        if self.posicion_actual < len(self.lexemas):
            self.token_actual = self.lexemas[self.posicion_actual][1]  # Guarda solo el componente léxico
            self.posicion_actual += 1
        else:
            self.token_actual = EOF

    def analizar_archivo(self):
        conjunto_sgte = [EOF]
        self.json(conjunto_sgte)

    def json(self, synchset):
        conjunto_prim = [simbolos["{"], simbolos["["]]  # ["L_LLAVE", "L_CORCHETE"]
        if self.token_actual in conjunto_prim:
            self.element()
        else:
            pass # TODO: Error sintáctico

    def element(self, synchset):
        conjunto_prim = [simbolos["{"], simbolos["["]]
        conjunto_sgte = [simbolos[","], simbolos["]"], simbolos["}"], EOF]
        self.check_input(conjunto_prim, conjunto_sgte)
        if(self.token_actual == simbolos["{"]):
            self.object(conjunto_sgte)
        elif(self.token_actual == simbolos["["]):
            self.array(conjunto_sgte)
        else:
            pass # TODO: Error sintáctico
        self.check_input(conjunto_sgte, conjunto_prim)

    def object(self, synchset):
        pass

    def array(self, synchset):
        pass

    def element_list(self, synchset):
        pass

    def element_list_aux(self, synchset):
        pass

    def attribute_list(self, synchset):
        pass

    def attribute_list_aux(self, synchset):
        pass

    def attribute(self, synchset):
        pass

    def attribute_name(self, synchset):
        pass

    def attribute_value(self, synchset):
        pass

    # Funciones para Panic Mode
    def error(self):
        pass

    def check_input(self, firsts, follows):
        if self.token_actual not in firsts:
            self.error()
            self.scanto(firsts + follows)

    def scanto(self, synchset):
        while self.token_actual not in (synchset + [EOF]):
            self.get_token()