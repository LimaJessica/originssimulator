import random
from abc import ABC, abstractmethod
from arma import Arma

class Inimigo(ABC):
    def __init__(self,
        classe:str, id:None, nivel:int, nome:None,
        dano_simples:float,dano_carregado:float,
        respawnavel:bool,barra_hp:float,arma:Arma):
        
        self.classe=classe
        self.nome=nome
        self.nivel=nivel
        self.id=id
        self.dano_simples=dano_simples
        self.dano_carregado=dano_carregado
        self.respawnavel=respawnavel
        self.barra_hp=barra_hp
        self.arma=arma

    def exibir_info(self):
        if self.classe=='Comum':
            print('Atenção! Inimigo nas redondezas!')
            print('Relaxe, é um inimigo comum!')
        else:
            print(f'Nome: {self.nome} | Classe: {self.classe}')
        print(f'Nível: {self.nivel}')
        print(f'Barra de hp: {self.barra_hp}')
        #print(f'Arma de eleição: {self.arma.nome}')
        print('___Estatísticas de dano corpo-a-corpo___')
        print(f'Golpe simples: {self.dano_simples} | Golpe carregado: {self.dano_carregado}')
        print('')

class InimigoComum(Inimigo):
    def gerar_inimigo_comum(n:int):
        #A classe cliente informa o nível desejado para o inimigo
        #e os danos simples e carregado são calculados em cima disso
        arma=Arma.carregar_por_id(0)
        ds=n*10
        dc=n*15
        ic=Inimigo('Comum',None,1,'Inimigo comum',ds,dc,False,500,arma)
        return ic

class Phylake(Inimigo):
    #def gerar_phylake():
    def __init__(self,id:int,nivel:int,nome:str,
        dano_simples:float,dano_carregado:float,vivo:bool,barra_hp:float,arma:Arma):
        self.classe='Phylake'
        self.respawnavel=True

        self.nome=nome
        self.id=id
        self.nivel=nivel
        self.dano_simples=dano_simples
        self.dano_carregado=dano_carregado
        self.vivo=vivo
        self.barra_hp=barra_hp
        self.arma=arma
        

    def exibir_info(self):
        super().exibir_info()

    def gerar_por_id(i:int):
        import json
        arq=json.load(open('./json/phylakes.json'))
        phylake=None
        for p in arq:
            if p['id']==i:
                arma=Arma.carregar_por_id(p['id_arma'])
                phylake=Phylake(
                        p['id'],
                        p['nivel'],
                        p['nome'],
                        p['dano_simples'],
                        p['dano_carregado'],
                        p['vivo'],
                        p['barra_hp'],
                        arma)
                        #id,nivel,nome,dano_simples,dano_carregado,arma
        if phylake==None:
            print(f'Não foi possível encontrar nenhum Phylake com o id {i}')
            #Percorreu o json inteiro e não encontrou phylake com esse id OU encontrou e ele já estava morto
            #Nesse caso, será tratado no método que randomiza o id
        return phylake