import random
from random import sample
from enum import Enum
from protagonista import Protagonista
from comandos import Comando
from arma import Arma
from inimigos import Inimigo, InimigoComum, Phylake
from inimigo_factory import InimigoFactory

#PARA REFERÊNCIA:
#
#r: resultado da execução de um método (retornará 0 em caso de sucesso ou 1 em caso de erro) para tratamento por parte da classe app
#inv: quantidade de comandos inválidos do usuário
#j:jogador
#ia: inimigo atual

teclas_ataque=['q','w','e','r','a','s','d','f']
instancias_disponiveis=['defendendo','vulnerável','contra-atacando']
contraataques_disponiveis=['simples','carregado']
class CombateStrategy():
    def iniciar_jogo(self,jogador:Protagonista):
        inimigo=self.selecao_de_inimigo(jogador)
        equipamento=self.selecao_de_equipamento(jogador)
        
        print('')
        print('Agora que você já selecionou seu equipamento, vamos a um breve tutorial.')
        comandos=Comando.carregar_comandos_por_json()
        print('Digite ESC a qualquer momento para encerrar o jogo.')

        self.iniciar_combate(jogador,inimigo,equipamento)
        #self.exibir_tutorial(comandos)
        
    def processar_comando(self,c:str,j:Protagonista,i:Inimigo,equip):
        #print(f'Você selecionou o comando {c}')
        comando=Comando.buscar_por_tecla(c)
        if(comando==None):
            print('Comando inválido')
        else:
            instancia_inimigo=random.sample(instancias_disponiveis,1)[0]
            if(instancia_inimigo=='defendendo'):
                if(c not in teclas_ataque):
                    print(f'Você optou por não investir contra {i.nome}')
                else:
                    print(f'Ataque frustrado! {i.nome} está se defendendo.')
            if(instancia_inimigo!='defendendo'):
                print(f'{i.nome} está vulnerável!')
                #if(comando.tecla in teclas_ataque):
                if(c in teclas_ataque):
                    if(c=='a'):
                        print(f'{comando.mensagem} {equip[0]["nome"]}')
                        i.barra_hp=i.barra_hp-(j.dano_simples*equip[0]['multiplicador_de_dano'])
                    if(c=='s'):
                        print(f'{comando.mensagem} {equip[0]["nome"]}')
                        i.barra_hp=i.barra_hp-(j.dano_carregado*equip[0]['multiplicador_de_dano'])
                    if(c=='d'):
                        print(f'{comando.mensagem} {equip[1]["nome"]}')
                        i.barra_hp=i.barra_hp-(j.dano_simples*equip[1]['multiplicador_de_dano'])
                    if(c=='f'):
                        print(f'{comando.mensagem} {equip[1]["nome"]}')
                        i.barra_hp=i.barra_hp-(j.dano_carregado*equip[1]['multiplicador_de_dano'])
                    if(c=='q'):
                        print(f'{comando.mensagem} {equip[2]["nome"]}')
                        i.barra_hp=i.barra_hp-(j.dano_simples*equip[2]['multiplicador_de_dano'])
                    if(c=='w'):
                        print(f'{comando.mensagem} {equip[2]["nome"]}')
                        i.barra_hp=i.barra_hp-(j.dano_carregado*equip[2]['multiplicador_de_dano'])
                    if(c=='e'):
                        print(f'{comando.mensagem} {equip[3]["nome"]}')
                        i.barra_hp=i.barra_hp-(j.dano_simples*equip[3]['multiplicador_de_dano'])
                    if(c=='r'):
                        print(f'{comando.mensagem} {equip[3]["nome"]}')
                        i.barra_hp=i.barra_hp-(j.dano_carregado*equip[3]['multiplicador_de_dano'])
                    print(f'{i.nome} ainda possui {round(i.barra_hp)} de vida!')
                else:
                    print(f'{comando.mensagem}')
            if(instancia_inimigo=='contra-atacando'):
                c2=input(f'Rápido! {i.nome} está contra-atacando. Defenda-se!').lower()
                if((c2=='1')or(c2=='3')):
                    print('Excelente!')
                    if(c2=='1'):
                        print(f'{j.nome} bloqueou o contra-ataque!')
                    if(c2=='3'):
                        print(f'{j.nome} aparou o contra-ataque!')
                else:
                    print(f'Essa não! {j.nome} está vulnerável!')
                    reacao=random.sample(contraataques_disponiveis,1)[0]
                    if(reacao=='simples'):
                        j.hp-=i.dano_simples
                        print(f'{j.nome} acaba de sofrer {i.dano_simples} de dano!')
                    else:
                        j.hp-=i.dano_carregado
                        print(f'{j.nome} acaba de sofrer {i.dano_carregado} de dano!')
                    j.checar_estado()

    def iniciar_combate(self,j:Protagonista,i:Inimigo,equip):
        print('')
        print(f'Hora de acabar com o {i.nome}, {j.nome}!')
        comando_usuario=''
        while((j.vivo==True)and(comando_usuario!='esc')):
            if(i.barra_hp>0):
                #print(f'Vida atual do {i.nome}: {i.barra_hp}')
                comando_usuario=input('Seu comando: ').lower()
                if(comando_usuario=='esc'):
                    print('Encerrando o jogo...')
                    break
                else:
                    self.processar_comando(comando_usuario,j,i,equip)
            else:
                print(f'{i.nome} está morto!')
                break
            
    def exibir_tutorial():#(self,comandos:Comando):
        print('')
        print('Agora que você já selecionou seu equipamento, vamos a um breve tutorial.')
        print('É importante que você preste bastante atenção, pois durante o combate, após cada um de seus comandos, é possível que o inimigo contra-ataque.')
        #for c in comandos:
            #c.exibir_info()

    def selecao_de_equipamento(self,j:Protagonista):
        print(f'Você possui 4 espaços livres para equipar o armamento que desejar.')
        print(f'Escolha sabiamente, pois estas armas te acompanharão até sua morte')
        slot=1
        armas_equipadas=[]
        while(slot<=4):
            print('')
            print(f'Selecione a arma que você deseja equipar no slot {slot}')
            if((slot==1)or(slot==2)):
                print('Este espaço é reservado para arcos, e você pode carregar dois deles')
                print('')
                registros_por_classe=Arma.apresentar_armas_por_classe(3)
                print('')
                escolha=input('Digite o id do arco que você gostaria de equipar: ')
                aenc=Arma.carregar_por_id(int(escolha))
                inv=0
                while(aenc==None):
                    escolha=input('Informe o id da arma novamente: ')
                    inv+=1
                    if(inv==5):
                        print('Não estamos chegando a lugar algum. Encerrando o jogo...')
                        break
                if(aenc!=None):
                    armas_equipadas.append(aenc)
                print('')
            else:
                print('Este espaço é reservado para armas de combate corpo-a-corpo')
                print('(Dica: nada te impede de equipar duas armas do mesmo tipo nos slots de número 3 e 4, mas é altamente recomendado que você opte por variedade)')
                #1=longa cortante,2=longa contundente,3=arco,4=espada
                while(slot<=4):
                    print('As classes de arma disponíveis são:')
                    print('[1] Longas cortantes')
                    print('[2] Longas contundentes')
                    print('[3] Espadas e demais armas curtas')
                    escolha=input('Informe o número do tipo de arma que você gostaria de equipar:')
                    inv2=0
                    while(((escolha!='1')and(escolha!='2'))and(escolha!='3')):
                        escolha=input('Opção inválida. Por favor, escolha um valor de 1 a 3: ')
                        inv2+=1
                        if(inv2==5):
                            print('Não estamos chegando a lugar algum. Encerrando o jogo...')
                            break
                    if(escolha=='1'):
                        print('')
                        registros_por_classe=Arma.apresentar_armas_por_classe(1)
                        escolha=input('Digite o id da arma longa cortante que você gostaria de equipar: ')
                        aenc=Arma.carregar_por_id(int(escolha))
                        inv=0
                        while(aenc==None):
                            escolha=input('Informe o id da arma novamente: ')
                            inv+=1
                            if(inv==5):
                                print('Não estamos chegando a lugar algum. Encerrando o jogo...')
                                break
                        if(aenc!=None):
                            armas_equipadas.append(aenc)
                    else:
                        if(escolha=='2'):
                            print('')
                            registros_por_classe=Arma.apresentar_armas_por_classe(2)
                            escolha=input('Digite o id da arma longa contundente que você gostaria de equipar:')
                            aenc=Arma.carregar_por_id(int(escolha))
                            inv=0
                            while(aenc==None):
                                escolha=input('Informe o id da arma novamente: ')
                                inv+=1
                                if(inv==5):
                                    print('Não estamos chegando a lugar algum. Encerrando o jogo...')
                                    break
                            if(aenc!=None):
                                armas_equipadas.append(aenc)
                        else:
                            print('')
                            registros_por_classe=Arma.apresentar_armas_por_classe(4)
                            escolha=input('Digite o id da espada que você gostaria de equipar:')
                            aenc=Arma.carregar_por_id(int(escolha))
                            inv=0
                            while(aenc==None):
                                escolha=input('Informe o id da arma novamente: ')
                                inv+=1
                                if(inv==5):
                                    print('Não estamos chegando a lugar algum. Encerrando o jogo...')
                                    break
                            if(aenc!=None):
                                armas_equipadas.append(aenc)
                    slot+=1
                    print('')
                #registros_por_classe=Arma.apresentar_armas_por_classe(id_classe)
            slot+=1
        print('')
        print('Aqui está seu equipamento:')
        slot=1
        for ae in armas_equipadas:
            print(f'SLOT #{slot}::::::::::::::::::::::::::::::::::::::')
            arma=Arma(ae['id'],ae['id_classe'],ae['nome'],ae['raridade'],ae['tipo'],ae['multiplicador_de_dano'],ae['descricao'])
            arma.exibir_info()
            print('')
            slot+=1
        return armas_equipadas


    def selecao_de_inimigo(self,j:Protagonista)->Inimigo:
        print('Inimigos na área:')
        print('[1] Inimigo comum')
        print('[2] Phylake')
        inv=0
        ia=None
        opcao=input('Selecione um tipo de inimigo a combater: ')
        while((opcao!='1')and(opcao!='2')):
            inv+=1
            if(inv>=5):
                print('Tá de brincadeira, né? Encerrando o jogo...')
                break
            print('Comando inválido. Por favor, escolha de acordo com as opções disponíveis')
            opcao=input()
        if(opcao=='1'):
            print('Você escolheu combater um inimigo comum. Frouxo!')
            ia=InimigoFactory.criar(1,j.nivel)
            ia.exibir_info()

        else:
            print('Você escolheu combater um Phylake')
            ia=InimigoFactory.criar(2,j.nivel)
            ia.exibir_info()
        return ia
    @staticmethod
    def atacar(comando:str):
        pass


