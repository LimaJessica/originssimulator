class Classes_Armas:
    def __init__(self,id:int,nome:str,descricao:str):
        self.id=id
        self.nome=nome
        self.descricao=descricao
    
    def exibirinfo(self):
        print(f'Classe de armas #{self.id}: {self.nome}')
        print(f'Descrição: {self.descricao}')
        print('')
    def carregarjson():
        import json
        arq=json.load(open('./json/classes_armas.json'))
        classes=[]
        for c in arq:
            classes.append(c)
        return classes