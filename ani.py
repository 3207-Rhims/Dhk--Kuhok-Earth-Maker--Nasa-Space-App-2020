
import math, random, sys
import pygame
from pygame.locals import *
import time

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

# define display surface			
W, H = 1200,650
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Surviving In Mars")
FPS = 500

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

bg = pygame.image.load("/Users/Arafat/Desktop/himel/hellow world.cpp/himel.py/nasa game/img/bang.png").convert()
bgWidth, bgHeight = bg.get_rect().size

stageWidth = bgWidth * 2
stagePosX = 0

startScrollingPosX = HW

circleRadius = 10
circlePosX = circleRadius
playerImg=pygame.image.load("/Users/Arafat/Desktop/himel/hellow world.cpp/himel.py/nasa game/man.png").convert()
playerPosX = circleRadius
playerPosY = 385
playerVelocityX = 0

font=pygame.font.SysFont(None,25)
def message(msg,color):
    screen_text=font.render(msg,True,color)
    DS.blit(screen_text, [int(W/10),int(H/15)])
    

def player(playerPosX,playerPosY):
    playerVelocityX = 0
    DS.blit(playerImg, (playerPosX,playerPosY))

# main loop
while True:
	events()

	k = pygame.key.get_pressed()
	
	if k[K_RIGHT]:
		playerVelocityX = 1
	elif k[K_LEFT]:
		playerVelocityX = -1
	else:
		playerVelocityX = 0
		
	playerPosX += playerVelocityX
	if playerPosX > stageWidth - circleRadius: playerPosX = stageWidth - circleRadius
	if playerPosX < circleRadius: playerPosX = circleRadius
	if playerPosX < startScrollingPosX: circlePosX = playerPosX
	elif playerPosX > stageWidth - startScrollingPosX: circlePosX = playerPosX - stageWidth + W
	else:
		circlePosX = startScrollingPosX
		stagePosX += -playerVelocityX
	
	rel_x = stagePosX % bgWidth
	DS.blit(bg, (rel_x - bgWidth, 0))
	if rel_x < W:
		DS.blit(bg, (rel_x, 0))
    
	stagePosX-=1
	DS.blit(playerImg, (int(circlePosX), int(playerPosY) - 25))
	
	if k[K_CAPSLOCK]:
		p=message("Let the journey begin,press A", BLACK) 
       
    #level-2
	if k[K_a]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/earth-1.jpg").convert()
		bg=exp
		#z=message("new mars for press b", BLACK)
		#p=z       
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("want to do photosyntheis and make live in earth? ...Yes for press:B  No for press:C ", WHITE) 		
		pygame.display.update()  
    #level-3               
	if k[K_b]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/simple.png").convert()
		bg=exp   
		#message("Wanna Plant some trees and want to mars too healthy for survive ? Press:C for YES OR Press:b for NO", BLACK)    
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("""Humans are coming in world...
          Press : D""", BLACK)  
		
		pygame.display.update()	
  	#level-4
	if k[K_c]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/level-17.png").convert()
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(1000)
		message("Game OVER",BLACK)
		pygame.display.update()    
	if k[K_d]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/fire@.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Want to start agriculture? ...Press E for YEs,Press 5 for NO(3sec)",BLACK)
		pygame.display.update()   
	if k[K_e]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/agriculture.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("End of an Ice Age...for next level info push F 3sec",BLACK)
		pygame.display.update()          
	if k[K_f]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/ice.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("want to build home? YES for Press:G or No Press:C",BLACK)
		pygame.display.update() 
	if k[K_g]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/build.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Want to invent sciene invention? Press: H for Yes Pres:5 for No ",BLACK)
		pygame.display.update()  
	if k[K_h]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/science.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Want to build Village or City ? Press: I for village and Press: L for city",BLACK)
		pygame.display.update()  
	if k[K_i]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/village.jpg").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Want to grow some crops? Press:J for yes Press:5 for NO",BLACK)
		pygame.display.update()  
	if k[K_j]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/sciagri.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Want to Growing more harvest using science? Press:K for yes Press:5 for NO(3sec) ",BLACK)
		pygame.display.update()   
	if k[K_k]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/food.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("People need more Food,need to use fertilizer.Want to build fertilizer factory? Yes:M or No:C ",BLACK)
		pygame.display.update()     
	if k[K_l]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/city.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Wanna build some industry for need? press:M for yes or Press:5 for NO",BLACK)
		pygame.display.update()   
	if k[K_m]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/factory.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message(" new life or want to build more industry to be modern?  ...Press:N for new life and Press:O for modern(3sec)",BLACK)
		pygame.display.update() 
	if k[K_n]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/level-6.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Shortage Food...For food Press:J or Press:O  ",WHITE)
		pygame.display.update() 
	if k[K_o]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/air.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Too much pollution...Press:P to continue or Press:R for plan tree",WHITE)
		pygame.display.update()
	if k[K_p]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/industry.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Too Much water pollution for industry...Press:Q for continue Press:S for clean beach and water",WHITE)
		pygame.display.update()      
	if k[K_r]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/plant.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Too Much water pollution for industry clean beach and water for Press:S or Press:T",WHITE)
		pygame.display.update()    
	if k[K_s]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/beach.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("A new beach...Press:U",WHITE)
		pygame.display.update() 
	if k[K_t]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/flood.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Too much damage in case of  Flood ...Press: V to next(3sec)",WHITE)
		pygame.display.update()
	if k[K_u]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/nicebeach.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("People need to Industry for basic need...Press:W (3sec) ",WHITE)
		pygame.display.update()  
	if k[K_v]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/storm.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Press:C(3sec)",WHITE)
		pygame.display.update()  
	if k[K_w]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/sea.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Too Much plastic pollution Or build space station..to see Press:Y Or Press:X",WHITE)
		pygame.display.update() 
	if k[K_x]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/space.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Need to develop biodegradable energy to sustain ..Press:Z for yes Press:C for NO",WHITE)
		pygame.display.update()  
	if k[K_y]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/plastic.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("need to build some biodigradble energy..Press:Z for yes or Press:C for no",WHITE)
		pygame.display.update()   
	if k[K_z]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/bio.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("eco frdly indutsry...Pres:1 for yes or press:C",WHITE)
		pygame.display.update()  
	if k[K_1]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/eco.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("A new city Pres:2 ...",WHITE)
		pygame.display.update() 
	if k[K_2]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/city2.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("need to build more industry for basic need cause natural energy is not much...Pres:3",WHITE)
		pygame.display.update() 
	if k[K_3]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/sea.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("need to cut to produce jalani...Pres:4",WHITE)
		pygame.display.update() 
	if k[K_4]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/cut.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("with plustic on ocean,heat rising and temperature ,earth...Pres:t",WHITE)
		pygame.display.update() 
	if k[K_5]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/die.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Game Over....people are died for FOOD",BLACK)
		pygame.display.update()    
  
  
       
      
   
          
   
        
                                        
        				        		        
	pygame.display.update()
 
	CLOCK.tick(FPS)
	DS.fill(BLACK)