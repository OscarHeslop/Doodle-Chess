#displaying the board - make it pure python 

#is 8x8 grid 


import pygame
import sys
import numpy as np





# 1. Initialize Pygame
pygame.init()

#IS 8 by 8
screen_width, screen_height = 800,800
ROWS, COLS = 8, 8
square_size = int(screen_width / ROWS)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Oscars RL Chess")

#----------------------------
#ALL SQUARE COLOURS
#----------------------------




colour_1 = pygame.Color("#32a852") #green 
colour_2 = pygame.Color("#3244a8") #blue
move_square_colour = pygame.Color("#f5427e") #pink


def draw_board():
    for r in range(ROWS):
        for c in range(COLS):
            if (r + c) % 2 == 0:
                square_colour = colour_1
            else:
                square_colour = colour_2
                
            # Calculate position dynamically based on grid index
            x = c * square_size

            y = r * square_size
            
            # Draw the square onto the screen
            pygame.draw.rect(screen, square_colour, (x, y, square_size, square_size))


#--------------------------
# ! MAIN GAME LOOP
#--------------------------


#--------------------------
# ! SETTING THE VARS
#--------------------------

x = None
y = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        #ALL INPUTS CHECKED HERE 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 1 means Left Click
                # Get the raw pixel coordinates (e.g., x=450, y=120)
                mouse_x, mouse_y = event.pos
                
                # Convert pixels to chess grid coordinates (0 to 7)
                clicked_col = int(mouse_x // square_size)
                clicked_row = int(mouse_y // square_size)


                x = (clicked_col) * square_size
                y = (clicked_row) * square_size


                
                
                print(f"Pixel Clicked: ({mouse_x}, {mouse_y})")




    draw_board()    
    if (x != None) and (y != None):
        pygame.draw.rect(screen, move_square_colour, (x, y, square_size, square_size))
    
    

   



    pygame.display.flip()

# Clean exit
pygame.quit()
sys.exit()
