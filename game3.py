import pygame 

def main(): 
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('loading... a meme')

    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'yellow': (255, 255, 0),
        'white': (255, 255, 255),

    }

    current_color = colors['white']

    x,y = 30,30
    sprite_width , height = 60,60
    clock = pygame.time.Clock()
    done = False
    while not done :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            x -= 3
        if pressed[pygame.K_RIGHT]:
            x += 3
        if pressed[pygame.K_UP]:
            y -= 3
        if pressed[pygame.K_DOWN]:
            y += 3

        x = min(max(0,x), SCREEN_WIDTH - sprite_width)
        y = min(max(0,y), SCREEN_HEIGHT - height)
    
        if x==0: current_color = colors['blue']
        elif x == SCREEN_WIDTH - sprite_width: current_color = colors['yellow']
        elif y == 0: current_color = colors['red']
        elif y == SCREEN_HEIGHT - height: current_color = colors['green']
        else:
         current_color = colors['white']

        screen.fill((0,0,0))

        pygame.draw.rect(screen, current_color, (x,y,sprite_width,height))
        pygame.display.flip()
        clock.tick(90)
    pygame.quit()
if __name__ == "__main__":
    main()