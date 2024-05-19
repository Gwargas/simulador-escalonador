class Memoria_RAM:
    capacidade = 34359738368  # 32Gbytes

    def adicionar_processo(self):
        ...
    # Enviar processo para memória secundária
    def swapp_out(self):
        ...

class Memoria_secundaria:
    # O armazenamento será mesmo infinito?
    armazenamento = []
    def adicionar_processo(self):
        ...
    # Enviar processo para memória primária
    def swapp_in(self):
        ...

class Processo:
    def __init__(self, chegada, fase1, entrada_saida, fase2, tamanho, disco):
        self.c = chegada
        self.f1 = fase1
        self.io = entrada_saida 
        self.f2 = fase2
        self.tam = tamanho  # Em Mbytes
        self.d = disco
    def mbytes_para_bytes(self):
        return (self.tam * 1048576)
    def enviar_memoria_primaria(self):
        ...

class Processador:
    def __init__(self, identificador):
        self.id = identificador 

class Computador:
    ram = Memoria_RAM()
    cpu1 = Processador('cpu1')
    cpu2 = Processador('cpu2')
    cpu3 = Processador('cpu3') 
