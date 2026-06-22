class Quarto:
    # método construtor
    def __init__(self, id, tipo, valor)>
        self.id = id
        self.tipo = tipo
        self.__valor = valor
        self.disponivel = True

    def exibir_detalhes(self):
        print(f'''Quarto {self.id} - {self.tipo})
Valor: {self.__valor}
Disponível: {self.disponivel}''')

    def reservar(self):
        if (self.disponivel == True):
            self.disponivel = False
            print("O quarto foi reservado com sucesso!")
        else:
            print("O quarto está indisponível!")

    def liberar(self):

        
