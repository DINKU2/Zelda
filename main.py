import pygame, sys
from settings import *
from debug import debug
from level import Level

class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('My Zelda')
		self.clock = pygame.time.Clock()
  
		self.level = Level()
  
		main_sound = pygame.mixer.Sound('all_graphic/audio/main.ogg')
		main_sound.set_volume(.02)
		main_sound.play(loops=-1)
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_TAB:
						self.level.toggle_menu()

			self.screen.fill(WATER_COLOR)
			self.level.run()
			#debug('what is happening here')
			pygame.display.update()
			self.clock.tick(FPS) 

if __name__ == '__main__':
	game = Game()
	game.run()	               