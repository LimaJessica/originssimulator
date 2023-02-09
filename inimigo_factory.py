import random
from random import sample
from enum import Enum
from abc import ABC, abstractmethod
from inimigos import Inimigo, InimigoComum, Phylake

phylakes_disponiveis=[1,2,3,4,5,6,7,8,9,10]

class TipoInimigo(Enum):
    COMUM=1
    PHYLAKE=2
    #Futuramente
    #OCULTO=3
class InimigoFactory:
    @staticmethod
    def criar(tipo_inimigo:int, nivel_jogador:int)->Inimigo:
        print('Randomizando inimigo a ser combatido...')

        if tipo_inimigo==TipoInimigo.COMUM.value:
            return InimigoComum.gerar_inimigo_comum(nivel_jogador)
        if tipo_inimigo==TipoInimigo.PHYLAKE.value:
            #"epv" abaixo significa "encontrou phylake vivo", solução temporária para facilitar o laço while abaixo sem ter que instanciar um phylake vazio antes
            # (construtor de Phylakes não permitiria)
            epv=False
            while epv==False:
                #print('Randomizando Phylake...')
                id_aleatorio=random.sample(phylakes_disponiveis,1)[0]
                #print(f'Buscando phylake de id {id_aleatorio}')
                print('')
                p=Phylake.gerar_por_id(id_aleatorio)
                if p==None:
                    pass
                    #print(f'Phylake não encontrado, buscando outro...')
                else:
                    print('Atenção! Phylake por perto!')
                    if p.vivo==True:
                        epv=True
                    else:
                        print(f'Phylake {p.nome} encontrado! Mas esse você já matou =(')
                        print('Buscando outro...')
            return p