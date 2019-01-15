import pygame
import time
import random

pygame.init()

screen = pygame.display.set_mode((1000,700))
blue = 0,0,255
black = 0,0,0
green = 0,255,10
grass = 0,128,0
sky = (22,187,185)
white = [255,255,255]
pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 30)
c1x, c1y = 10,250
c2x, c2y = 80, 250
c3x, c3y = 150, 250
cax, cay = 775, 250
cbx, cby = 840, 250
ccx, ccy = 915, 250
m1x, m1y = 10, 150
m2x, m2y = 80, 150
m3x, m3y = 150, 150
mxa, may = 775, 150
mbx, mby = 840, 150
mcx , mcy = 915, 150
b1x = 250


boatval1= 270,245
boatval2 = 320, 245
boatval3 = 370, 245
boatval1a = 730, 245
boatval2a = 680, 245
boatval3a = 630, 245
lc, lm , rc, rm = 0,0,0,0			

screen.fill(white)

class State:
	def __init__(self, leftcannibal, leftmissionary, rightcannibal, rightmissionary, boat):
		self.leftcannibal = leftcannibal
		self.leftmissionary = leftmissionary
		self.rightcannibal = rightcannibal
		self.rightmissionary = rightmissionary
		self.boat = boat
	
	def is_goal(self):
		if self.leftcannibal == 0 and self.leftmissionary == 0:
			return True
		else:
			return False 
	def is_valid(self):
		if self.missionaryLeft >= 0 and self.missionaryRight >= 0 \
                   and self.leftcannibal >= 0 and self.rightcannibal >= 0 \
                   and (self.leftmissionary == 0 or self.leftmissionary >= self.leftcannibal) \
                   and (self.rightmissionary == 0 or self.rightmissionary >= self.rightcannibal):
			return True
		else:
			return False

	

def game_event(current_state):
	new_state = current_state

	while True:
		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
						
			def go(curr_state, lc, lm, rc, rm):	
							
				if current_state.boat == 'left':
					new_state = State(curr_state.leftcannibal-lc, curr_state.leftmissionary-lm, curr_state.rightcannibal+rc, curr_state.rightmissionary+rm, 'right')
				else:
					new_state = State(curr_state.leftcannibal+lc, curr_state.leftmissionary+lm, curr_state.rightcannibal-rc, curr_state.rightmissionary-rm, 'left')
				return new_state


				

			def mouse_click(current_state):
				global c1x, c1y, c2x, c2y, c3x, c3y, m1x, m1y, m2x, m2y, m3x, m3y, boatval1, boatval2,boatval3, boatval1a, boatval2a
				global lc, lm, rc, rm , b1x, b2x, b1y , cax, cbx, ccx, cay, cby, ccy, mxa, may, mbx, mby, mcx, mcy
				global new_state
				cannibal = pygame.image.load ('cannibal.jpg').convert()
				missionary = pygame.image.load('missionary.jpg').convert()
				ca= screen.blit(cannibal, (c1x, c1y))
				cb= screen.blit(cannibal, (c2x, c2y))
				cc = screen.blit(cannibal, (c3x, c3y))
				ma= screen.blit(missionary, (m1x, m1y))
				mb= screen.blit(missionary, (m2x, m2y))
				mc= screen.blit(missionary, (m3x, m3y))
			
				
				
				boat = pygame.image.load('boat.png').convert()
				screen.blit(boat, (b1x, 350))

				
				mouse = pygame.mouse.get_pos()
				click = pygame.mouse.get_pressed()
				

				textsurface = myfont.render('go!!', False, (0, 0, 0))
				screen.blit(textsurface, (455,450))
				#mouse click for left cannibal
				if 55+c1x > mouse[0] > c1x and 100+c1y > mouse[1] > c1y:
					
					if click[0] == 1:
						lc, lm, rc, rm = lc+1, lm+0, rc+1 ,rm+0
						c1x, c1y = boatval1
						pygame.time.delay(500)	
						
				
				if 55+c2x > mouse[0] > c2x and 100+c2y > mouse[1] > c2y:
					if click[0] == 1:
						lc, lm, rc, rm= lc+1, lm+0, rc+1 ,rm+0
						c2x, c2y = boatval2
						pygame.time.delay(500)
						
				if 55+c3x > mouse[0] > c3x and 100+c3y > mouse[1] > c3y:
					if click[0] == 1:
						lc, lm, rc, rm= lc+1, lm+0, rc+1 ,rm+0	
						c3x, c3y = boatval3
					
						pygame.time.delay(500)
						
				#mouse click for left missionary 
				if 55+m1x > mouse[0] > m1x and 100+m1y > mouse[1] > m1y:
					if click[0] == 1:
						lc, lm, rc, rm= lc+0, lm+1, rc+0 ,rm+1
						m1x, m1y = boatval1
						pygame.time.delay(500)
				if 55+m2x > mouse[0] > m2x and 100+m2y > mouse[1] > m2y:
					if click[0] == 1:
						lc, lm, rc, rm= lc+0, lm+1, rc+0 ,rm+1
						m2x, m2y = boatval2
						pygame.time.delay(500)
				if 55+m3x > mouse[0] > m3x and 100+m3y > mouse[1] > m3y:
					if click[0] == 1:
						lc, lm, rc, rm= lc+0, lm+1, rc+0 ,rm+1
						m3x, m3y = boatval3
						pygame.time.delay(500)
						
				#mouse click for right cannibal
				if 55+cax > mouse[0] > cax and 100+cay > mouse[1] > cay:
					
					if click[0] == 1:
						lc, lm, rc, rm = lc+1, lm+0, rc+1 ,rm+0
						c1x, c1y = boatval1a
						pygame.time.delay(500)	
						
				
				if 55+cbx > mouse[0] > cbx and 100+cby > mouse[1] > cby:
					if click[0] == 1:
						lc, lm, rc, rm= lc+1, lm+0, rc+1 ,rm+0
						c2x, c2y = boatval2a
						pygame.time.delay(500)
						
				if 55+ccx > mouse[0] > ccx and 100+ccy > mouse[1] > ccy:
					if click[0] == 1:
						lc, lm, rc, rm= lc+1, lm+0, rc+1 ,rm+0	
						c3x, c3y = boatval3a
					
						pygame.time.delay(500)
						
				#mouse click for right missionary 
				if 55+mxa> mouse[0] > mxa and 100+may > mouse[1] > may:
					if click[0] == 1:
						lc, lm, rc, rm= lc+0, lm+1, rc+0 ,rm+1
						mxa,may = boatval1a
						pygame.time.delay(500)
						
				if 55+mbx > mouse[0] > mbx and 100+mby > mouse[1] > mby:
					if click[0] == 1:
						lc, lm, rc, rm= lc+0, lm+1, rc+0 ,rm+1
						mbx, mby = boatval2a
						pygame.time.delay(500)
				if 55+mcx > mouse[0] > mcx and 100+mcy > mouse[1] > mcy:
					if click[0] == 1:
						lc, lm, rc, rm= lc+0, lm+1, rc+0 ,rm+1
						mcx, mcy = boatval3a
						pygame.time.delay(500)
						
					
													
				#mouse click left boat to bank
				if 270+55 > mouse[0] > 270 and 345 > mouse[1] > 245:
					if click[0] == 1:
						if (m1x == 270 and c1x == 270):
							m1x, m1y = 10, 150
							c1x, c1y = 10, 250 
						else:
							if (m1x == 270):
								m1x, m1y = 10, 150
							if (c1x == 270):
								c1x, c1y = 10, 250 
						
						
				if 320+55 > mouse[0] > 320 and 345 > mouse[1] > 245:
					if click[0] == 1:
						if (m2x == 320 and c2x == 320):
							m2x, m2y = 80, 150
							c2x, c2y = 80, 250 
						else:
							if (m2x == 320):
								m2x, m2y = 80, 150
							elif (c2x == 320):
								c2x, c2y = 80, 250 
						pygame.time.delay(500)
						
				if 370+55 > mouse[0] > 370 and 345 > mouse[1] > 245:
					if click[0] == 1:
						if (m3x == 370 and c3x == 370):
							m3x, m3y = 150, 150
							c3x, c3y = 150, 250 
						else:
							if (m3x == 370):
								m3x, m3y = 150, 150
							elif (c3x == 370):
								c3x, c3y = 150, 250 
						print (m1x, m2x, m3x)
						pygame.time.delay(500)
						
				#mouse click right boat to bank
				if 785 > mouse[0] > 730 and 345 > mouse[1] > 245:
					if click[0] == 1:
						if (m1x == 730 and c1x == 730):
							m1x, m1y = 775, 150
							c1x, c1y = 775, 250
						else:
							if (m1x == 730):
								m1x, m1y = 775, 150
							if (c1x == 730):
								c1x, c1y = 775, 250 
							
						
				if 735 > mouse[0] > 680 and 345 > mouse[1] > 245:
					if click[0] == 1:
						if (m2x == 680 and c2x == 680):
							m2x, m2y = 840, 150
							c2x, c2y = 840, 250
						else:
							if (m2x == 680):
								m2x, m2y = 840, 150
							elif (c2x == 680):
								c2x, c2y = 840, 250 
						pygame.time.delay(500)
						
				if 685 > mouse[0] > 630 and 345 > mouse[1] > 245:
					if click[0] == 1:
						if (m3x == 630 and c3x == 630):
							m3x, m3y = 915, 150
							c3x, c3y = 915, 250
						else:
							if (m3x == 630):
								m3x, m3y = 915, 150
							elif (c3x == 630):
								c3x, c3y = 915, 250 
						
						pygame.time.delay(500)
				
				#mouse click for right cannibal
				if 55+cax > mouse[0] > cax and 100+cay > mouse[1] > cay:
					
					if click[0] == 1:
						lc, lm, rc, rm = lc+1, lm+0, rc+1 ,rm+0
						cax, cay = boatval1a
						pygame.time.delay(500)
			
				if 55+cbx > mouse[0] > cbx and 100+cby > mouse[1] > cby:
					
					if click[0] == 1:
						lc, lm, rc, rm = lc+1, lm+0, rc+1 ,rm+0
						cbx, cby = boatval2a
						pygame.time.delay(500)
	
				if 55+ccx > mouse[0] > ccx and 100+ccy > mouse[1] > ccy:
					
					if click[0] == 1:
						lc, lm, rc, rm = lc+1, lm+0, rc+1 ,rm+0
						ccx, ccy = boatval3a
						pygame.time.delay(500)
				
				
						
				
				
				#go button		
				if 455+50 > mouse[0] > 455 and 450+50 > mouse[1] > 450:	
				
					pygame.draw.rect (screen, green, (455, 450, 50,50))
					if click[0] == 1:
						if (c1x == 270):
							c1x, c1y = boatval1a
						if (c2x == 320):
							c2x, c2y = boatval2a
						if (c3x == 370):
							c3x, c3y = boatval3a
						
						if m1x == 270:
							m1x, m1y = boatval1a
						if m2x == 320:
							m2x, m2y = boatval2a
						if m3x == 370:
							m3x, m3y = boatval3a
						
						new_current_state = go(current_state, lc, lm, rc, rm)
						
						current_state = new_current_state
						
						lc, lm, rc, rm = 0,0,0,0
						print (str(current_state.leftcannibal) + "    " +str (current_state.leftmissionary) +"     "+ str(current_state.rightcannibal) +"    " +str(current_state.rightmissionary)+"   " + str(current_state.boat))
			
						pygame.time.delay(500)
					else:
						if (current_state.boat == 'right'):
							b1x = 600
									
						else: 
							b1x = 250
							
					if current_state.is_valid == True:
						if current_state.is_goal == True:
								winner = myfont.render('Winner', False, (0, 0, 0))
								screen.blit(gameover, (455,450))
							
						else: 
							gameover = myfont.render('Game Over', False, (0, 0, 0))
							screen.blit(gameover, (455,450))
				else:
					pygame.draw.rect (screen, sky, (455, 450, 50,50))
					
				
				return current_state
				
				
	


			def background_image():
				pygame.draw.polygon(screen, grass, ((0,200), (300,200),(150,700), (0,700)), 0)
				pygame.draw.polygon(screen, grass, ((1000,200), (700,200),(850,700), (1000,700)), 0)
				pygame.draw.polygon(screen, blue, ((300,200),(700,200),(850,700),(150,700)), 0)
				pygame.draw.polygon(screen, sky , ((0,0),(1000,0),(1000,200),(0,200)),0)
		
			#images          
			background_image()
			state = mouse_click(new_state)
			new_state = state
			pygame.display.flip()
	
	
def main():
	initial_state = State(3, 3 ,0,0, 'left')   
	state = game_event(initial_state)


main()

		
		
	
