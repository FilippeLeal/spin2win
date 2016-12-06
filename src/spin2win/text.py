import pygame
import time
black = (0,0,0)
white = (255,255,255)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
	
def message_display(x, y, text, test):
		gameDisplay = pygame.display.set_mode((800,650), 0, 32)
		gameDisplay.fill((255, 255, 255))
		largeText = pygame.font.Font('freesansbold.ttf', 35)
		TextSurf, TextRect = text_objects(text, largeText)
		TextRect.center = ((x),(y))
		gameDisplay.blit(TextSurf, TextRect)
		rect = pygame.Rect(0, 600, 800, 50)
		pygame.display.update(rect)
		
		