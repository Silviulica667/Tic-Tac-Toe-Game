import pygame 
import random
from sys import exit

pygame.init() #tutorial
screen = pygame.display.set_mode((1000, 600)) #tutorial
pygame.display.set_caption("X SI 0") #tutorial
clock = pygame.time.Clock() #tutorial

test_font = pygame.font.Font(None, 70) #tutorial
test_font1 = pygame.font.Font(None, 35) #tutorial

font = test_font.render('X si 0', False, 'White') #tutorial

vsplayer = test_font1.render('Versus Player', False, 'White')   
vscomputer = test_font1.render('Versus Computer', False, 'White')   
reset = test_font1.render('Reset Score', False, 'White')

fundal = pygame.image.load('Fundal/stea.png')
gameover = pygame.image.load('Fundal/GameOver.png').convert_alpha()
tryagain =  pygame.image.load('Fundal/TryAgain.png').convert_alpha()
zero = pygame.image.load('Fundal/CercAlbastru.png').convert_alpha()
patrat = pygame.image.load('Fundal/Patrat.png').convert_alpha()

tryagain_rect = tryagain.get_rect(center = (150 ,550))
tryagain_rectAI = tryagain.get_rect(center = (850 ,550))
fundal_rect = fundal.get_rect(center = (500, 300))
vsplayer_rect = vsplayer.get_rect(center=(150, 500)) 
vscomputer_rect =  vscomputer.get_rect(center=(850, 500))
reset_rect =  reset.get_rect(center=(500, 525))

lista_rect = []
for i in range (9):
    lista_rect.insert(i, zero.get_rect(center = (100+i*100, 50)))
    
lista_rect1 = []
for i in range (9):
    lista_rect1.insert(i, patrat.get_rect(center = (100+i*100, 550)))    

fundal_animat_list = []   
for i in range (7): fundal_animat_list.insert(i, pygame.image.load('Fundal/Stelutza.png'))
x = [x*100 for x in range (7)]
y = [x*60 for x in range (7)]  

def animatie_stele(): 
       
    for i in range (7): screen.blit(fundal_animat_list[i],(x[i]-100, y[i]-100))   
         
    for i in range (7):
        
        if(i%2==0):
            x[i] += i-1.5
            y[i] += i-4.5   
        
        if(i%2==1):  
                
            y[i] += i-2.2
            x[i] -= i-2.5
            
        if(x[i] >= 1001): 
            x[i] = 1 
        if(x[i] <= 0): 
            x[i] = 1000      
    
        if(y[i] >= 701):
            y[i] = 1 
        if(y[i] <= 0):
            y[i] = 700         

tabla_list_1 = []
tabla_list_2 = []
tabla_list_3 = []

w = [1 * i for i in range (9)]
v = [1 * i for i in range (9)]
w1 = [1 * i for i in range (9)]
v1 = [1 * i for i in range (9)]

list_random = [(380,200),(485, 200),(588,200),(380,305),(485,305),(588,305),(380,409),(485,409),(588,409)]   
     
def funtie_tabla(c1, c2, c3, c4, c5, c6, lista, win, j):

    alabama = lista[i]

    if (alabama.centerx > c1 and alabama.centerx < c2 and alabama.centery > c3 and alabama.centery < c4):
            alabama.center= (c5, c6) 
            win[j] = 10  

def funtie_tablaAI(c1, c2, c3, c4, c5, c6, lista, win, j, c7 ,c8):

    alabama = lista[i]

    if (alabama.centerx > c1 and alabama.centerx < c2 and alabama.centery > c3 and alabama.centery < c4):
            alabama.center= (c5, c6) 
            win[j] = 10 
      
            lista_rect1[j].center = (c7, c8)
               
            for m in range (9):
                for k in range (9):
                       
                    if lista_rect1[j].center == lista_rect[m].center:  
                        lista_rect1[j].center = (c7+104, c8)
                        if lista_rect1[j].centerx >= 630:
                            lista_rect1[j].center = (c7-208, c8)
                
                            if lista_rect1[j].colliderect(lista_rect1[k]):  
                                lista_rect1[j].center = (c7+104, c8)
                                if lista_rect1[j].centerx >= 630:
                                    lista_rect1[j].center = (c7-208, c8)
                                            
def functie_repetare(o, p, functie1, functie2, cx, cy):
    if functie1[o].center == functie2[p].center:
        functie1[o].center = (cx,cy)
   
moving = False #tutorial
game_active = False
ai_mode = True

rand = 0
score= 0
score1 = 0
numaratoare = 0

while True: 
    
    for event in pygame.event.get():  #tutorial
        if event.type == pygame.QUIT:  #tutorial
            pygame.quit()  #tutorial
            exit  #tutorial
    if ai_mode:
        if game_active == True:  #tutorial

            coordonate_tabla = pygame.Rect(330, 150, 300, 300)

            mouse = pygame.mouse.get_pos() 

            screen.blit(fundal,(fundal_rect))
                                    
            animatie_stele()
            
            for i in range (3): 
                pygame.draw.rect(screen, 'Gold', pygame.Rect(330+i*100, 150, 110, 110), 3)
                pygame.draw.rect(screen, 'Gold', pygame.Rect(330+i*100, 150+100, 110, 110), 3)          
                pygame.draw.rect(screen, 'Gold', pygame.Rect(330+i*100, 150+200, 110, 110), 3)
                pygame.draw.rect(screen, 'Purple', pygame.Rect(328+i*100, 148, 110, 110), 3)
                pygame.draw.rect(screen, 'Purple', pygame.Rect(328+i*100, 148+100, 110, 110), 3)          
                pygame.draw.rect(screen, 'Purple', pygame.Rect(328+i*100, 148+200, 110, 110), 3)
                pygame.draw.rect(screen, 'Red', pygame.Rect(332+i*100, 152, 110, 110), 3)
                pygame.draw.rect(screen, 'Red', pygame.Rect(332+i*100, 152+100, 110, 110), 3)          
                pygame.draw.rect(screen, 'Red', pygame.Rect(332+i*100, 152+200, 110, 110), 3)  
            
            for i in range(9):
                screen.blit(zero, lista_rect[i])
                screen.blit(patrat, lista_rect1[i])
        
        if game_active == True: #tutorial           
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                for i in range (9):
                    if lista_rect[i].collidepoint(event.pos) and rand == 0:
                        
                        alabama = lista_rect[i]
                        moving = True
                        
                    if lista_rect1[i].collidepoint(event.pos) and rand == 1:
                        
                        alabama = lista_rect1[i]
                        moving = True                 
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if coordonate_tabla.collidepoint(event.pos):
                    moving = False     
                        
            if event.type == pygame.MOUSEMOTION and moving:
                alabama.center = mouse 
            
            if event.type == pygame.MOUSEBUTTONUP:        
                
                for i in range (9):   

                    funtie_tabla(330, 430, 150, 250, 380, 200, lista_rect, v, 0)
                    funtie_tabla(430, 530, 150, 250, 485, 200, lista_rect, v, 1)
                    funtie_tabla(530, 630, 150, 250, 588, 200, lista_rect, v, 2)
                    funtie_tabla(330, 430, 250, 350, 380, 305, lista_rect, v, 3)
                    funtie_tabla(430, 530, 250, 350, 485, 305, lista_rect, v, 4)
                    funtie_tabla(530, 630, 250, 350, 588, 305, lista_rect, v, 5)
                    funtie_tabla(330, 430, 350, 450, 380, 409, lista_rect, v, 6)
                    funtie_tabla(430, 530, 350, 450, 485, 409, lista_rect, v, 7)
                    funtie_tabla(530, 630, 350, 450, 588, 409, lista_rect, v, 8)                                

                    funtie_tabla(330, 430, 150, 250, 380, 200, lista_rect1, w, 0)
                    funtie_tabla(430, 530, 150, 250, 485, 200, lista_rect1, w, 1)
                    funtie_tabla(530, 630, 150, 250, 588, 200, lista_rect1, w, 2)
                    funtie_tabla(330, 430, 250, 350, 380, 305, lista_rect1, w, 3)
                    funtie_tabla(430, 530, 250, 350, 485, 305, lista_rect1, w, 4)
                    funtie_tabla(530, 630, 250, 350, 588, 305, lista_rect1, w, 5)
                    funtie_tabla(330, 430, 350, 450, 380, 409, lista_rect1, w, 6)
                    funtie_tabla(430, 530, 350, 450, 485, 409, lista_rect1, w, 7)
                    funtie_tabla(530, 630, 350, 450, 588, 409, lista_rect1, w, 8) 
            
                    moving = False

                    if lista_rect[i].centerx > 330 and lista_rect[i].centerx < 630 and lista_rect[i].centery > 150 and  lista_rect[i].centery < 450:
                        if rand == 0:
                            for k in range (9):
                                functie_repetare(0, k, lista_rect, lista_rect1, 100, 300) 
                                functie_repetare(1, k, lista_rect, lista_rect1, 100, 300)     
                                functie_repetare(2, k, lista_rect, lista_rect1, 100, 300)     
                                functie_repetare(3, k, lista_rect, lista_rect1, 100, 300)     
                                functie_repetare(4, k, lista_rect, lista_rect1, 100, 300)     
                                functie_repetare(5, k, lista_rect, lista_rect1, 100, 300)     
                                functie_repetare(6, k, lista_rect, lista_rect1, 100, 300)     
                                functie_repetare(7, k, lista_rect, lista_rect1, 100, 300)     
                                functie_repetare(8, k, lista_rect, lista_rect1, 100, 300)            
                        rand = 1
                            
                    if lista_rect1[i].centerx > 330 and lista_rect1[i].centerx < 630 and lista_rect1[i].centery > 150 and lista_rect1[i].centery < 450: 
                    
                        if rand == 1:
                            for h in range (9):
                                functie_repetare(0, h, lista_rect1, lista_rect, 800, 300) 
                                functie_repetare(1, h, lista_rect1, lista_rect, 800, 300)     
                                functie_repetare(2, h, lista_rect1, lista_rect, 800, 300)     
                                functie_repetare(3, h, lista_rect1, lista_rect, 800, 300)     
                                functie_repetare(4, h, lista_rect1, lista_rect, 800, 300)     
                                functie_repetare(5, h, lista_rect1, lista_rect, 800, 300)     
                                functie_repetare(6, h, lista_rect1, lista_rect, 800, 300)     
                                functie_repetare(7, h, lista_rect1, lista_rect, 800, 300)     
                                functie_repetare(8, h, lista_rect1, lista_rect, 800, 300)                          
                        rand = 0
                        
            if v[0] == v[1] == v[2] or v[3] == v[4] == v[5] or v[6] == v[7] == v[8] or v[0] == v[3] == v[6] or v[1] == v[4] == v[7] or v[2] == v[5] == v[8] or v[0] == v[4] == v[8] or v[2] == v[4] == v[6]:
                
                game_active = False  #tutorial
                score += 1
               

            if w[0] == w[1] == w[2] or w[3] == w[4] == w[5] or w[6] == w[7] == w[8] or w[0] == w[3] == w[6] or w[1] == w[4] == w[7] or w[2] == w[5] == w[8] or w[0] == w[4] == w[8] or w[2] == w[4] == w[6]: 
            
                game_active = False  #tutorial
                score1 += 1
                
            print(rand) 
                   
        else: 
            
            score_text = test_font.render(f'{int(score)}', True, ('White'))   
            score_text1 = test_font.render(f'{int(score1)}', True, ('White')) 
            nume_text1 =  test_font.render('Zerouri', True, ('White'))   
            nume_text2 =  test_font.render('Patrate', True, ('White'))                             
            score_rect = score_text.get_rect(center = (450, 100))
            score_rect1 = score_text1.get_rect(center = (550, 100))
            score_rect3 = score_text.get_rect(center = (100, 100))
            score_rect4 = score_text1.get_rect(center = (750, 100))
        
            screen.blit(gameover, (0,0))
            screen.blit(vsplayer, vsplayer_rect)
            screen.blit(vscomputer, vscomputer_rect)
            screen.blit(reset, reset_rect)
            screen.blit(tryagain, tryagain_rect)
            screen.blit(tryagain, tryagain_rectAI)
            screen.blit(score_text, score_rect)
            screen.blit(score_text1, score_rect1)
            screen.blit(nume_text1, score_rect3)
            screen.blit(nume_text2, score_rect4)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tryagain_rect.collidepoint(event.pos):
                    game_active = True 
                    w = [1 * i for i in range (9)]
                    v = [1 * i for i in range (9)]
                    rand = 0
                    for i in range(9):
                        lista_rect[i].center = (100+i*100, 50) 
                        lista_rect1[i].center = (100+i*100, 550)
                                  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tryagain_rectAI.collidepoint(event.pos): 
                    ai_mode = False
                    game_active = True 
                    rand = 0
                    w = [1 * i for i in range (9)]
                    v = [1 * i for i in range (9)]    
                    for i in range(9):
                        lista_rect[i].center = (100+i*100, 50) 
                        lista_rect1[i].center = (100+i*100, 550)
                          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_rect.collidepoint(event.pos): 
                    score = 0
                    score1 = 0
                                                      
#A.I. CODE                                   
    else:
        rand = 0 
        if game_active == True:  #tutorial

            coordonate_tabla = pygame.Rect(330, 150, 300, 300)

            mouse = pygame.mouse.get_pos() 

            screen.blit(fundal,(fundal_rect))
                                    
            animatie_stele()
            
            for i in range (3): 
                pygame.draw.rect(screen, 'Gold', pygame.Rect(330+i*100, 150, 110, 110), 3)
                pygame.draw.rect(screen, 'Gold', pygame.Rect(330+i*100, 150+100, 110, 110), 3)          
                pygame.draw.rect(screen, 'Gold', pygame.Rect(330+i*100, 150+200, 110, 110), 3)
                pygame.draw.rect(screen, 'Purple', pygame.Rect(328+i*100, 148, 110, 110), 3)
                pygame.draw.rect(screen, 'Purple', pygame.Rect(328+i*100, 148+100, 110, 110), 3)          
                pygame.draw.rect(screen, 'Purple', pygame.Rect(328+i*100, 148+200, 110, 110), 3)
                pygame.draw.rect(screen, 'Red', pygame.Rect(332+i*100, 152, 110, 110), 3)
                pygame.draw.rect(screen, 'Red', pygame.Rect(332+i*100, 152+100, 110, 110), 3)          
                pygame.draw.rect(screen, 'Red', pygame.Rect(332+i*100, 152+200, 110, 110), 3)
                     
            for i in range(9):
                screen.blit(zero, lista_rect[i])
                screen.blit(patrat, lista_rect1[i])
        
        if game_active == True:            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                for i in range (9):
                    if lista_rect[i].collidepoint(event.pos) and rand == 0:
                        
                        alabama = lista_rect[i]
                        moving = True
               
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if coordonate_tabla.collidepoint(event.pos):
                                moving = False     
                        
            if event.type == pygame.MOUSEMOTION and moving:  
                alabama.center = mouse 
            
            if event.type == pygame.MOUSEBUTTONUP:        
 
                    for i in range (9):  
                        if rand == 0:
                            funtie_tablaAI(330, 430, 150, 250, 380, 200, lista_rect, v1, 0, 588, 410)
                            funtie_tablaAI(430, 530, 150, 250, 484, 200, lista_rect, v1, 1, 380, 200)
                            funtie_tablaAI(530, 630, 150, 250, 588, 200, lista_rect, v1, 2, 484, 305)
                            funtie_tablaAI(330, 430, 250, 350, 380, 305, lista_rect, v1, 3, 484, 410)
                            funtie_tablaAI(430, 530, 250, 350, 484, 305, lista_rect, v1, 4, 588, 305)
                            funtie_tablaAI(530, 630, 250, 350, 588, 305, lista_rect, v1, 5, 484, 200)
                            funtie_tablaAI(330, 430, 350, 450, 380, 410, lista_rect, v1, 6, 588, 200) 
                            funtie_tablaAI(430, 530, 350, 450, 484, 410, lista_rect, v1, 7, 380, 305)
                            funtie_tablaAI(530, 630, 350, 450, 588, 410, lista_rect, v1, 8, 380, 410)                                
                        moving = False    
                            
            if v1[0] == v1[1] == v1[2] or v1[3] == v1[4] == v1[5] or v1[6] == v1[7] == v1[8] or v1[0] == v1[3] == v1[6] or v1[1] == v1[4] == v1[7] or v1[2] == v1[5] == v1[8] or v1[0] == v1[4] == v1[8] or v1[2] == v1[4] == v1[6]:
                
                game_active = False
                score += 1

            if w[0] == w[1] == w[2] or w[3] == w[4] == w[5] or w[6] == w[7] == w[8] or w[0] == w[3] == w[6] or w[1] == w[4] == w[7] or w[2] == w[5] == w[8] or w[0] == w[4] == w[8] or w[2] == w[4] == w[6]: 
            
                game_active = False
                score1 += 1
                             
        else:
             
            score_text = test_font.render(f'{int(score)}', True, ('White'))   
            score_text1 = test_font.render(f'{int(score1)}', True, ('White')) 
            nume_text1 =  test_font.render('Zerouri', True, ('White'))   
            nume_text2 =  test_font.render('Patrate', True, ('White'))                             
            score_rect = score_text.get_rect(center = (450, 100))
            score_rect1 = score_text1.get_rect(center = (550, 100))
            score_rect3 = score_text.get_rect(center = (100, 100))
            score_rect4 = score_text1.get_rect(center = (750, 100))
            
            screen.blit(gameover, (0,0))
            screen.blit(vsplayer, vsplayer_rect)
            screen.blit(vscomputer, vscomputer_rect)
            screen.blit(reset, reset_rect)
            screen.blit(tryagain, tryagain_rect)
            screen.blit(tryagain, tryagain_rectAI)
            screen.blit(score_text, score_rect)
            screen.blit(score_text1, score_rect1)
            screen.blit(nume_text1, score_rect3)
            screen.blit(nume_text2, score_rect4)
                     
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tryagain_rectAI.collidepoint(event.pos):
                    game_active = True
                    rand = 0 
                    w1 = [1 * i for i in range (9)]
                    v1 = [1 * i for i in range (9)] 
                    for i in range(9):
                        lista_rect[i].center = (100+i*100, 50) 
                        lista_rect1[i].center = (100+i*100, 550)
                              
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tryagain_rect.collidepoint(event.pos): 
                    ai_mode = True
                    game_active = True   
                    rand = 0
                    w1 = [1 * i for i in range (9)]
                    v1 = [1 * i for i in range (9)]    
                    for i in range(9):
                        lista_rect[i].center = (100+i*100, 50) 
                        lista_rect1[i].center = (100+i*100, 550)  
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_rect.collidepoint(event.pos): 
                    score = 0
                    score1 = 0
                                                        
    pygame.display.update() #tutorial
    clock.tick(120)  #tutorial