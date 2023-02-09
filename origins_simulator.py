import pygame
pygame.init()
x=400
y=300
velocidade=10
bayek=pygame.image.load("imagens/bayek.png")
janela=pygame.display.set_mode((1280,980))
pygame.display.set_caption("Origins Simulator")

janela_aberta=True
while janela_aberta:
    janela.blit(bayek,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            janela_aberta=False

    pygame.display.update()
        
pygame.quit()