from protagonista import Protagonista
from inimigos import Inimigo, InimigoComum, Phylake
from inimigo_factory import InimigoFactory
from classes_armas import Classes_Armas
from combate import CombateStrategy
import random
#SINGLETON: OK
#FACTORY: OK
#STRATEGY:
if __name__=='__main__':
    jogador=Protagonista.carregar_dados_base()
    jogador.exibir_info()
    #(1):::::::::::::::::::::SINGLETON:::::::::::::::::::::
    #TESTANDO SINGLETON:
    #j2=Protagonista.carregar_dados_base()
    #print(id(jogador))
    #print(id(j2))
    #FUNCIONOU

    #(3):::::::::::::::::::::STRATEGY::::::::::::::::::::::
    cs=CombateStrategy()

    cs.iniciar_jogo(jogador)
    #cs.selecao_de_inimigo(jogador,r)
    #cs.selecao_de_equipamento(jogador)

    #(2)::::::::::::::::::::::FACTORY::::::::::::::::::::::
    #FUNCIONANDO! Aqui foi apenas um teste inicial, agora o Factory está sendo acionado dentro do método selecao_de_inimigo no arquivo combate.py
    #inimigoatual=InimigoFactory.criar(1,jogador.nivel)
    #inimigoatual.exibir_info()
    #inimigoatual=InimigoFactory.criar(2,jogador.nivel)
    #inimigoatual.exibir_info()

    