import pygame
import colours
def textScreenTitle(text,colour,x,y, titleFont,gameWindow):
    screen_text = titleFont.render(text,True,colour)
    gameWindow.blit(screen_text,(x,y))
def textScreenInst(text,colour,x,y,howToPlayFont, gameWindow):
    screen_text = howToPlayFont.render(text,True,colour)
    gameWindow.blit(screen_text,(x,y))
def textScreen(text,colour,x,y, font, gameWindow):
    screen_text = font.render(text,True,colour)
    gameWindow.blit(screen_text,(x,y))

def plotSnake(points, gameWindow, snake_length, snake_width):
    for i in range(len(points)):
        pygame.draw.rect(gameWindow,colours.red,pygame.Rect([points[i][0],points[i][1],snake_length,snake_width]))
        if i==0:
            pygame.draw.rect(gameWindow,colours.black,pygame.Rect([points[i][0],points[i][1],20,20]))
            pygame.draw.rect(gameWindow,colours.red,pygame.Rect([points[i][0],points[i][1],20,20]))