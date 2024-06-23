from tablaSimbolos import simbolos
EOF = ""

class AnalizadorSintactico:
    def __init__(self, lexemas):
        self.lexemas = lexemas
        self.posicion_actual = 0
        self.token_actual = None
        self.errores = []
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
            self.error()
            

    def element(self):
        conjunto_prim = [simbolos["{"], simbolos["["]]
        conjunto_sgte = [simbolos[","], simbolos["]"], simbolos["}"], EOF]
        self.check_input(conjunto_prim, conjunto_sgte)
        if(self.token_actual == simbolos["{"]):
            self.object(conjunto_sgte)
        elif(self.token_actual == simbolos["["]):
            self.array(conjunto_sgte)
        else:
            self.error()
        self.check_input(conjunto_sgte, conjunto_prim)
        

    def object(self, synchset):
        conjunto_prim = [simbolos["{"]]
        conjunto_sgte = [simbolos[","], simbolos["]"], simbolos["}"], EOF]
        self.check_input(conjunto_prim,synchset)
        if self.token_actual == simbolos["{"]:
            self.match(simbolos["{"], conjunto_sgte)
            self.attribute_list([simbolos["}"]] + conjunto_sgte)
            self.match(simbolos["}"], conjunto_sgte)
        self.check_input(conjunto_sgte, conjunto_prim)

    def array(self, synchset):
        conjunto_prim = [simbolos["["]]
        conjunto_sgte = [simbolos[","], simbolos["]"], simbolos["}"], EOF]
        self.check_input(conjunto_prim, conjunto_sgte)
        if self.token_actual == simbolos["["]:
            self.match(simbolos["["], conjunto_sgte)
            self.element_list([simbolos["]"]] + conjunto_sgte)
            self.match(simbolos["]"], conjunto_sgte)
        self.check_input(conjunto_sgte, conjunto_prim)

    def element_list(self, synchset):
        conjunto_prim = [simbolos["{"], simbolos["["]]
        conjunto_sgte = [simbolos["]"]]
        self.check_input(conjunto_prim, conjunto_sgte)
        if self.token_actual in conjunto_prim:
            self.element(synchset)
            self.element_list_aux(synchset)
        self.check_input(conjunto_sgte, conjunto_prim)
        pass

    def element_list_aux(self, synchset):
        conjunto_prim = [simbolos[","]]
        conjunto_sgte = [simbolos["]"]]
        self.check_input(conjunto_prim, conjunto_sgte)
        if self.token_actual == simbolos[","]:
            self.match(simbolos[","])
            self.element(conjunto_sgte)
            self.element_list_aux(synchset)
        self.check_input(conjunto_sgte, conjunto_prim)
        pass

    def attribute_list(self, synchset):
        conjunto_prim = [simbolos["string"]]
        conjunto_sgte = [simbolos["}"]]
        self.check_input(conjunto_prim, conjunto_sgte)
        if self.token_actual == simbolos["string"]:
            self.attribute(synchset)
            self.attribute_list_aux(synchset)
        self.check_input(conjunto_sgte, conjunto_prim)
        pass

    def attribute_list_aux(self, synchset):
        conjunto_prim = [simbolos[","]]
        conjunto_sgte = [simbolos["}"]]
        self.check_input(conjunto_prim, conjunto_sgte)
        if self.token_actual == simbolos[","]:
            self.match(simbolos[","])
            self.attribute(synchset)
            self.attribute_list_aux(synchset)
        self.check_input(conjunto_sgte, conjunto_prim)
        pass

    def attribute(self, synchset):
        conjunto_prim = [simbolos["string"]]
        conjunto_sgte = [simbolos[","], simbolos["}"]]
        self.check_input(conjunto_prim, conjunto_sgte)
        if self.token_actual == simbolos["string"]:
            self.attribute_name(synchset)
            self.match(simbolos[":"])
            self.attribute_value(synchset)
        self.check_input(conjunto_sgte, conjunto_prim)
        pass

    def attribute_name(self, synchset):
        conjunto_prim = [simbolos["string"]]
        conjunto_sgte = [simbolos[":"]]
        self.check_input(conjunto_prim, conjunto_sgte)
        if self.token_actual == simbolos["string"]:
            self.match(simbolos["string"])
        self.check_input(conjunto_sgte, conjunto_prim)
        pass

    def attribute_value(self, synchset):
        conjunto_prim = [simbolos["{"], simbolos["["], simbolos["string"], simbolos["number"], simbolos["true"], simbolos["false"], simbolos["null"]]
        conjunto_sgte = [simbolos[","], simbolos["}"]]
        self.check_input(conjunto_prim, conjunto_sgte)
        if self.token_actual in conjunto_prim:
            if self.token_actual == simbolos["{"] or self.token_actual == simbolos["["]:
                self.element(synchset)
            elif self.token_actual == simbolos["string"]:
                self.match(simbolos["string"])
            elif self.token_actual == simbolos["number"]:
                self.match(simbolos["number"])
            elif self.token_actual == simbolos["true"]:
                self.match(simbolos["true"])
            elif self.token_actual == simbolos["false"]:
                self.match(simbolos["false"])
            elif self.token_actual == simbolos["null"]:
                self.match(simbolos["null"])
        else:
            self.error()
        self.check_input(conjunto_sgte, conjunto_prim)
        pass

    # Funciones para Panic Mode
    def error(self):
        self.errores.append(f"Error sintáctico en token {self.token_actual} en posición {self.lexemas[self.posicion_actual][0]}")


    def check_input(self, firsts, follows):
        if self.token_actual not in firsts:
            self.error()
            self.scanto(firsts + follows)

    def scanto(self, synchset):
        while self.token_actual not in (synchset + [EOF]):
            self.get_token()

    def match(self, expected_token):
        if self.token_actual == expected_token:
                self.get_token()
        else:
            self.error()