class Cachorro:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando


    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo {alimento}.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False


c1 = Cachorro('Jorginho',12)

c1.comer("Feijão")
c1.parar_comer()
c1.parar_comer()
c1.comer("Maçã")



'''class Cachorro:
    def falar(self):
        print('Cachorro está falando...')

c1 = Cachorro()
c2 = Cachorro()

c1.falar()'''