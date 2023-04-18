# Exercício de adivinhação - 13/04/2023 - Amanda Louise Costa Nascimento
import sys
import random

class first_exception(Exception): pass

class adivinhacao:

    def __init__(self, valor=random.randint(1,10), count_try=1):
        self.count_try = count_try
        self.valor = valor

    def gera_novo_random(self):
        self.count_try = 1
        self.valor = random.randint(1,10)
        print('CRIANDO NOVO VALOR ALEATÓRIO...')
        #print(self.valor) usado para validar o codigo
        return self.valor
    
    def recebe_valor():
        num = int(input("Insira um valor de 1 à 10: "))
        return num
    
    def confere_first(self, num=int, count_try=int, valor=int):
        try:
            if (count_try == 1 and num == valor):
                raise first_exception(" VOCÊ TEM PODERES PSÍQUICOSSSS ")
        except first_exception as erro:
                print(erro)
                self.gera_novo_random()
                self.tentativas()
        except Exception as e:
                print("Erro Inesperado")
    
    def confere_igualdade(self, num=int, valor=int):
        try:
            if num == valor:
                print("FINALMENTE ACERTOU, MISERÁVEL !")
                self.gera_novo_random()
                self.tentativas()
        except:
                print("Erro Inesperado2")

    def tentativas(self):
        num = adivinhacao.recebe_valor()
        #print("TESTE:")
        #print(num)
        #print(self.count_try) # usados para validar o codigo
        #print(self.valor)
        
        adivinhacao.confere_first(self, num, self.count_try, self.valor)
        adivinhacao.confere_igualdade(self, num, self.valor)

        while num != self.valor:
            try:
                self.count_try = self.count_try+1
                self.tentativas()
            except:
                print("Erro Inesperado3")


if __name__ == "__main__":
    valor_recebido = adivinhacao()
    valor_recebido.tentativas()