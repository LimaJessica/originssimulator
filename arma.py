class Arma():
    def __init__(self,id:int,id_classe:int,nome:str,raridade:str,tipo:str,multiplicador_de_dano:int,descricao:str):
        self.id=id
        self.id_classe=id_classe
        self.nome=nome
        self.raridade=raridade
        self.tipo=tipo
        self.multiplicador_de_dano=multiplicador_de_dano
        self.descricao=descricao
    def exibir_info(self):
        print(f'Nome: {self.nome} | Raridade: {self.raridade} | ID: {self.id}')
        print(f'Tipo: {self.tipo} | Multiplicador de dano: {self.multiplicador_de_dano}')
        print(f'Descrição: {self.descricao}')
    def carregar_por_id(i:int):
        import json
        arq=json.load(open('./json/armas.json'))
        arma=None
        for a in arq:
            if a['id']==i:
                arma=a

        if(arma==None):
            print(f'Não foi possível encontrar arma com id {i} nos arquivos do jogo')
        return arma
    
    def apresentar_armas_por_classe(i: int):
        #1=longa cortante,2=longa contundente,3=arco,4=espada
        import json
        arq=json.load(open('./json/armas.json'))
        #Pensei em criar um vetor para armazenar todas as armas da classe buscada, mas
        #pensando melhor, não pareceu necessário, já que este método apenas exibe as armas,
        #para que o usuário visualize e informe o id da arma que quiser (e com base no id
        #informado, o método carregar_por_id sim se responsabiliza por trazer a arma

        #armas_encontradas=None
        qtde_armas_encontradas=0
        print('Exibindo armas disponíveis para a classe escolhida...')
        for a in arq:
            if(i==a['id_classe']):
                arma=Arma(a['id'],a['id_classe'],a['nome'],a['raridade'],a['tipo'],a['multiplicador_de_dano'],a['descricao'])
                print(f':::::::::::::::::ARMA #{arma.id}:::::::::::::::::')
                print(f'Nome: {arma.nome} | Raridade: {arma.raridade}')
                print(f'Tipo: {arma.tipo} | Multiplicador de dano: {arma.multiplicador_de_dano}')
                print(f'Descrição: {arma.descricao}')
                qtde_armas_encontradas+=1
                #armas_encontradas.append(arma)
        if(qtde_armas_encontradas==0):
            print('Não há registros de armas dessa classe nos arquivos do jogo')
        return qtde_armas_encontradas