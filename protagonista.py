class Protagonista:
    __instance=None
    #def __init__(self):
        #self.nome='Bayek 1 (teste)'
        #self.nivel=0
        #self.hp=200
        #self.xp=0
        #self.vivo=True
        #self.dano_simples=25
        #self.dano_carregado=50

        #self=self.carregar_dados_base
    def __init__(self,
    nome:str,nivel:int,
    hp:float,xp:float,
    vivo:bool,dano_simples:float,
    dano_carregado:float):
        self.nome=nome
        self.nivel=nivel
        self.hp=hp
        self.xp=xp
        self.vivo=vivo
        self.dano_simples=dano_simples
        self.dano_carregado=dano_carregado

    def __new__(cls,*args,**kwargs):
        if cls.__instance is None:
            cls.__instance=super().__new__(cls)
        return cls.__instance

    def checar_estado(self):
        if(self.hp<=0):
            self.vivo=False
            print(f'FIM DE JOGO! {self.nome} está {self.exibir_estado()}')
        else:
            print(f'{self.nome} ainda possui {self.hp}')
            
    def exibir_estado(self):
        if self.vivo==True:
            return 'vivo'
        else:
            return 'morto'

    def exibir_info(self):
        print(f'Nome: {self.nome}')
        print(f'Nível: {self.nivel} | XP: {self.xp}')
        print(f'Vida atual: {self.hp} ({self.exibir_estado()})')
        print('___Estatísticas de dano corpo-a-corpo___')
        print(f'Golpe simples: {self.dano_simples} | Golpe carregado: {self.dano_carregado}')
        print('')
    def carregar_dados_base():
        import json
        arq=json.load(open('./json/dados_base.json'))
        protagonista=None
        for dado in arq:
            if dado['categoria']=='PROTAGONISTA':
                #categoria, nome_protagonista, hp_base, xp_base, nivel_base, vivo
                protagonista=Protagonista(
                    dado['nome_protagonista'],
                    dado['nivel_base'],
                    dado['hp_base'],
                    dado['xp_base'],
                    dado['vivo'],
                    dado['dano_simples'],
                    dado['dano_carregado']
                )
        return protagonista