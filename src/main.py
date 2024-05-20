import queue

class Processo:
    def __init__(self, chegada, fase1, entrada_saida, fase2, tamanho, disco):
        self.c = chegada
        self.f1 = fase1
        self.io = entrada_saida 
        self.f2 = fase2
        self.tam = (tamanho * 1048576) # Em Mbytes
        self.d = disco
        self.p = 1 # Define a prioridade do processo, caso seja bloqueado p += 1, e sempre começa com 1
    def enviar_memoria_primaria(self):
        ...

class Memoria_RAM:
    capacidade = 34359738368  # 32Gbytes
    # Instanciando as quarto filas de processos prontos para serem executados 
    filas = [queue.Queue() for _ in range(4)]

    def adicionar_processo(self, processo: Processo):
        if (self.capacidade - processo.tam) < 0: # Caso não haja espaço na memória primária
            return -1
        if (processo.p == 1):
            self.filas[0].put(processo)
        elif (processo.p == 2):
            self.filas[1].put(processo)
        elif (processo.p == 3):
            self.filas[2].put(processo)
        elif (processo.p == 4):
            self.filas[3].put(processo)

    # Enviar processo para memória secundária
    def swapp_out(self):
        ...

class Memoria_secundaria:
    def __init__(self, identificador):
        self.id = identificador
        self.armazenamento = [] # O armazenamento será mesmo infinito?

    def adicionar_processo(self, processo: Processo):
        self.armazenamento.append(processo)

    # Enviar processo para memória primária
    def swapp_in(self):
        ...

class Processador:
    def __init__(self, identificador):
        self.id = identificador 

class Computador:
    # Inicialização da memória principal
    ram = Memoria_RAM()
    # Inicialização dos discos 
    disco1 = Memoria_secundaria('disco1')
    disco2 = Memoria_secundaria('disco2')
    disco3 = Memoria_secundaria('disco3')
    disco4 = Memoria_secundaria('disco4')
    # Inicialização dos processadores 
    cpu1 = Processador('cpu1')
    cpu2 = Processador('cpu2')
    cpu3 = Processador('cpu3') 
    cpu4 = Processador('cpu4')

    # Leitura do arquivo com cada um dos processos
    with open('input.txt', 'r') as arq:  
        for linha in arq:
            processo_linha = [x.split() for x in linha.split(',')]
            