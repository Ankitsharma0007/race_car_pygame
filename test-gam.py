import pygame,time,random,pdb
#pdb.set_trace()
pygame.init()

display_width = 600
display_height = 600

black= (0,0,0)
white=(200,25,25)
red = (255,0,0)
green = (0,200,0)
red1= (30,130,230)

car_width = 80
car_height= 80






gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Fast and Furious')

clock = pygame.time.Clock()



Carimg = pygame.image.load('racec.png')

def things_dodged(count):
    font= pygame.font.SysFont(None, 25)
    text = font.render("dodged :: " +str(count), True, black)
    gameDisplay.blit(text,(0,0))
    
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay,color, [thingx,thingy,thingw,thingh])


def car(x,y):
    gameDisplay.blit(Carimg,(x,y))

def text_object(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText= pygame.font.Font('freesansbold.ttf',80)
    TextSurf, TextRect = text_object(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(2)
    game_loop()

    

def crash():
    message_display('You Crashed')
    
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type==pygame.quit:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText= pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_object('Fast & Furious', largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        #print(mouse)

        if 150+100 > mouse[0]> 150 and 450+50 > mouse[1] > 450 :
            pygame.draw.rect(gameDisplay, red1,(150,450,100,50))
        else:            
            pygame.draw.rect(gameDisplay, green,(150,450,100,50))

        smallText= pygame.font.Font('freesansbold.ttf',20)
        TextSurf, TextRect = text_object('Go', smallText)
        TextRect.center = (((150+(100/2)),((450+(50/2)))))
        gameDisplay.blit(TextSurf, TextRect)


            

    #    smallText = pygame.font.Font("Freesansbold.ttf",20)
    #    TextSurf, TextRect = text_object("GO... !",smallText)
    #    TextRect.center = (((150+(100/2)),(450+(50/2)))
     #   gameDisplay.blit(TextSurf, TextRect)                  





        pygame.draw.rect(gameDisplay, red1,(400,450,100,50))





        
        pygame.display.update()
        clock.tick(15)
   


def game_loop():   

        x= (display_width * 0.45)
        y = (display_height * 0.7)

        x_change=0
        y_change=0

        thing_startx = random.randrange(0, display_width)
        thing_starty = -600
        thing_speed = 5
        thing_width = 50
        thing_height = 50
        dodged = 0


        gameExit = False

        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -5
                    elif event.key == pygame.K_RIGHT:
                        x_change = 5

                if event.type ==pygame.KEYUP:
                     if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                        x_change = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        y_change = -5
                    elif event.key == pygame.K_DOWN:
                        y_change = 5

                if event.type ==pygame.KEYUP:
                     if event.key == pygame.K_UP or event.key ==pygame.K_DOWN:
                        y_change = 0
                        

                        

            x += x_change
            y += y_change

            gameDisplay.fill(white)
            #things(thingx, thingy, thingw, thingh, color)
            things(thing_startx, thing_starty, thing_width, thing_height, black)
            thing_starty += thing_speed
            things_dodged(dodged)



            
            car(x,y)

            if x > display_width- car_width or x <0 :
                crash()
            if y > display_height- car_height or y <0 :
                crash()
              
            if thing_starty > display_height:
                thing_starty = 0 - thing_height
                thing_startx = random.randrange(0, display_width)
                dodged += 1
                thing_speed += 0.5
                thing_width += (dodged + 1.2)
                
            if y < thing_starty + thing_height:
             #   print('y crossover')
                if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx + thing_width :
                    
                    print('x crossover')
                    crash()
            pygame.display.flip()
            clock.tick(60)

#game_intro()    
game_loop()
pygame.quit()

quit()
     
            
