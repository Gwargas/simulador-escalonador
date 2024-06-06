import queue
import random

random.seed()

def gera_id():
    palavra = ""
    for i in range(50):
        letra = random.randint(33, 127)
        j = chr(letra)
        palavra += j
    return palavra

class PCB:
    def __init__(self, ident, p):
        self.estadoProcesso = "Novo"
        self.idProcesso = ident
        self.prioridade = p

class Processo:
    def __init__(self, chegada, fase1, entrada_saida, fase2, tamanho, disco):
        self.c = chegada
        self.f1 = fase1
        self.io = entrada_saida
        self.f2 = fase2
        self.tam = (tamanho * 1048576)  # Em Mbytes
        self.d = disco
        self.p = 1  # Define a prioridade do processo, caso seja bloqueado p += 1, e sempre começa com 1
        self.momento_saida = chegada + fase1 + entrada_saida + fase2  # TODO: Guardar quanto tempo o processo gasta em cada fase
        self.pcb = PCB(gera_id(), self.p)

    def enviar_memoria_primaria(self):
        ...

class Memoria_RAM:
    capacidade = 34359738368  # 32Gbytes
    filas = [queue.Queue() for _ in range(4)]  # Instanciando as quatro filas de processos prontos para serem executados
    bloqueados = []

    def adicionar_processo(self, processo: Processo):
        if (self.capacidade - processo.tam) < 0:  # Caso não haja espaço na memória primária
            return -1
        if (processo.p == 1):
            self.filas[0].put(processo)
        elif (processo.p == 2):
            self.filas[1].put(processo)
        elif (processo.p == 3):
            self.filas[2].put(processo)
        elif (processo.p == 4):
            self.filas[3].put(processo)

class Memoria_secundaria:
    bloqueados = []

    def __init__(self, identificador):
        self.id = identificador
        self.armazenamento = []  # O armazenamento será mesmo infinito?

    def adicionar_processo(self, processo: Processo):
        self.armazenamento.append(processo)

class Processador:
    def __init__(self, identificador):
        self.id = identificador

class Escalonador:
    def __init__(self, identificador):
        self.id = identificador

class Despachante(Escalonador):  # Curto Prazo
    def __init__(self, identificador):
        super(Despachante, self).__init__(identificador)  # Herdando do escalonador

    def Despacho(self):  # Seleciona processo para receber o estado de Executando
        ...

class MedioPrazo(Escalonador):
    def __init__(self, identificador):
        super(MedioPrazo, self).__init__(identificador)  # Herdando do escalonador

    def SwapOut(self, processo, ram, secundaria):  # RAM -> Mem.Sec.
        ...

    def Swapping(self, processo, ram, secundaria):  # Mem.Sec -> RAM; é preciso tirar o processo da lista de processos que estão na Mem.Sec. e jogá-lo pra lista da RAM
        ...

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
            # Further processing of processo_linha
