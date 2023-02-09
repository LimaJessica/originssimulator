class Comando():
    #def gerar_phylake():
    def __init__(self,id:int,tecla:str,mensagem:str,descricao:str):
        self.id=id
        self.tecla=tecla
        self.mensagem=mensagem
        self.descricao=descricao

    def exibir_info(self):
        print(f'{self.tecla} -> {self.descricao}')

    def carregar_comandos_por_json():
        import json
        arq=json.load(open('./json/comandos.json'))
        comandos=[]
        for c in arq:
            comando=Comando(c['id'],c['tecla'],c['mensagem'],c['descricao'])
            print(f'{comando.tecla} -> {comando.descricao}')
            comandos.append(comando)
        return comandos

    def buscar_por_tecla(t:str):
        import json
        arq=json.load(open('./json/comandos.json'))
        comando=None
        for c in arq:
            if(c['tecla']==t):
                comando=Comando(c['id'],c['tecla'],c['mensagem'],c['descricao'])
        return comando
class Save():
    pass
