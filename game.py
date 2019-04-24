import pygame, sys
from Actor import actor
from boat import boat
pygame.init()

display_width=1280

display_height=780

win=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Missionary and Cannibal (Dota 2 version)")
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
light_red=(226,110,110)

bgImg=pygame.image.load('river.png')
missImg=pygame.image.load('miss.png')
missImg1=pygame.image.load('miss1.png')
cannImg=pygame.image.load('cann.png')
cannImg1=pygame.image.load('cann1.png')
boatImg=pygame.image.load('boat.png')
goImg=pygame.image.load('go.png')
go1Img=pygame.image.load('go1.png')
losesnd=pygame.mixer.Sound('losesd.wav')
winsnd=pygame.mixer.Sound('winsd.wav')
diesnd=pygame.mixer.Sound('die.wav')
font=pygame.font.SysFont(None,25)

def main():

    x = (display_width * 0.1)
    y = (display_height * 0.8)
    x_change, y_change = 0, 0
    #creating missionaries and cannibals objects

    mc=[]
    mc.insert(0,actor(x-130,y-150,0,0,'M','left',missImg,missImg1, win))
    mc.insert(1,actor(x-70,y-150,0,0,'M','left',missImg,missImg1, win))
    mc.insert(2,actor(x-10,y-150,0,0,'M','left',missImg,missImg1, win))
    mc.insert(3,actor(x-130,y-230,0,0,'C','left',cannImg,cannImg1, win))
    mc.insert(4,actor(x-80,y-230,0,0,'C','left',cannImg,cannImg1, win))
    mc.insert(5,actor(x-30,y-230,0,0,'C','left',cannImg,cannImg1, win))
    
    #creating boat position objects
    boats=[]
    boats.insert(0,boat(127,478,2, missImg1, cannImg1, win))
    boats.insert(1,boat(626,478,3,missImg1, cannImg1, win))
    boats.insert(2,boat(288,478,4,missImg1, cannImg1, win))
    boats.insert(3,boat(787,478,5,missImg1, cannImg1, win))

    pygame.display.set_caption('Missionaries and cannibals (Dota 2 version)')
    clock = pygame.time.Clock()
    crashed = False
    boat_position = 0 #indicates boat at left shore
    a, b = 0, 0
    action = [a, b] #indicates no of missionaries and cannibals to move
    m, c, bt = 3, 3, 1 #indicates 3 missionaries, 3 canibals and boat at left shore
    state = [m, c, bt] #indicates state of missionaries, cannibals and boat at left shore

    gameover = False
    gameoverplayed,wonplayed=False,False
    left,right=False,False
    won=False
    moves=0 #for counting the no of moves

    #loading the background music
    # pygame.mixer.music.load('music/bgmusic.mp3')
    # pygame.mixer.music.play(-1) #play the bg music infinite times
    # sound=True
    while not crashed:
        #loading bgimage and new game image
        win.blit(bgImg, (0, 0))
        # win.blit(ngImg, (1000, 45))
        # if sound:
        #     win.blit(soundonImg, (1150, 40))
        # else:
        #     win.blit(soundoffImg, (1150, 40))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        #loading the missionaries and cannibals image
        for i in range(6):
            mc[i].display()

        #displaying states, actions, moves
        state_text = font.render("State: " + str(state), True, black)
        win.blit(state_text, [20, 20])
        action_text = font.render("Action: " + str(action), True, black)
        win.blit(action_text, [20, 50])
        moves_text = font.render("No. of moves: " + str(moves), True, black)
        win.blit(moves_text, [20, 80])
        cur = pygame.mouse.get_pos() #getting cursor position

        #click and point actions of sound button
        if 1150 + 50 > cur[0] > 1150 and 40 + 50 > cur[1] > 40:
            # if sound:
            #     win.blit(soundoffImg, (1150, 40))
            # else:
            #     win.blit(soundonImg, (1150, 40))

            if pygame.mouse.get_pressed() == (1, 0, 0):
                if sound:
                    sound=False
                    pygame.mixer.music.pause()
                else:
                    sound=True
                    pygame.mixer.music.play()

        #click and point actions of new game button
        if 800 + 150 > cur[0] > 800 and 55 + 55 > cur[1] > 55:
            # win.blit(ng1Img, (1000, 20))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                main()

        win.blit(boatImg, (x, y))  #display boat

        #checking gameover
        if (state[0] < state[1] and state[0]>0 )or  (state[0] > state[1] and state[0] < 3 ):
            # win.blit(gameoverImg, (400, 250))
            gameover = True

        #checking game won
        if state==[0,0,0] and action==[0,0]:
            # win.blit(wonImg, (400, 250))
            won=True


        if not gameover and not won:
            # click and point actions of go button
            if 590+88 > cur[0] > 590 and 300 + 90 > cur[1] > 300 and action != [0, 0]:
                win.blit(go1Img, (590, 300))
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    if boat_position == 0:
                        x_change = 10
                        for i in range(6):
                            if mc[i].pos == 2 or mc[i].pos == 4: mc[i].x_change = 10
                    else:
                        x_change = -10
                        for i in range(6):
                            if mc[i].pos == 3 or mc[i].pos == 5: mc[i].x_change = -10
            else:
                win.blit(goImg, (590, 300))

            #stopping condition of boat
            if x >= 580 and boat_position == 0:
                x_change = 0
                for i in range(6):
                    mc[i].x_change=0
                boat_position = 1
                moves+=1
                state[0], state[1], state[2] = state[0] - action[0], state[1] - action[1], 0
                for i in range(6):
                    if mc[i].pos == 2:
                        mc[i].pos = 3
                        mc[i].leftright = 'right'
                        mc[i].rect_x+=900
                    if mc[i].pos == 4:
                        mc[i].pos = 5
                        mc[i].leftright = 'right'
                        mc[i].rect_x += 900

            if x <= 100 and boat_position == 1:
                x_change = 0
                for i in range(6):
                    mc[i].x_change=0
                boat_position = 0
                moves+=1
                state[0], state[1], state[2] = state[0] + action[0], state[1] + action[1], 1

                for i in range(6):
                    if mc[i].pos == 3:
                        mc[i].pos = 2
                        mc[i].rect_x -= 900
                        mc[i].leftright = 'left'
                    if mc[i].pos == 5:
                        mc[i].pos = 4
                        mc[i].leftright = 'left'
                        mc[i].rect_x -= 900

            # if boat is not full
            if action != [1, 1] and action != [0, 2] and action != [2, 0]:
                for i in range(6):
                    # click and point actions of missionary or cannibal at ground
                    if mc[i].rect_x+actor.width > cur[0] > mc[i].rect_x and mc[i].rect_y+actor.height > cur[1] >mc[i].rect_y  :  
                        if mc[i].pos==0 and mc[i].leftright=='left' and boat_position==0:
                            mc[i].highlight()
                            if pygame.mouse.get_pressed() == (1, 0, 0):
                                if mc[i].char=='M':
                                    a+= 1
                                elif mc[i].char=='C':
                                    b+=1
                                if action == [0, 1] or action == [1, 0]:
                                    for k in range(6):
                                        if mc[k].pos == 2:
                                            left = True
                                        if mc[k].pos == 4:
                                            right = True
                                    if left:
                                        mc[i].x, mc[i].y = x + 180, y - 50
                                        mc[i].pos = 4

                                    elif right:
                                        mc[i].x, mc[i].y = x + 20, y - 50
                                        mc[i].pos = 2
                                else:
                                    mc[i].x, mc[i].y = x + 20, y - 50
                                    mc[i].pos = 2
                        elif mc[i].pos==1 and   mc[i].leftright == 'right' and boat_position == 1:
                            mc[i].highlight()
                            if pygame.mouse.get_pressed() == (1, 0, 0):
                                if mc[i].char == 'M':
                                    a += 1
                                elif mc[i].char == 'C':
                                    b += 1
                                if action == [0, 1] or action == [1, 0]:
                                    for k in range(6):
                                        if mc[k].pos == 3:
                                            left = True
                                        if mc[k].pos == 5:
                                            right = True
                                    if left:
                                        mc[i].x, mc[i].y = x + 180, y - 50
                                        mc[i].pos = 5
                                    elif right:
                                        mc[i].x, mc[i].y = x + 20, y - 50
                                        mc[i].pos = 3
                                else:
                                    mc[i].x, mc[i].y = x + 20, y - 50
                                    mc[i].pos = 3
                                print(i, mc[i].x, mc[i].y)

            # if any 1 or more actor on boat
            if action != [0, 0]:
                for j in range(4):
                    if boats[j].x + boat.width > cur[0] > boats[j].x and boats[j].y + boat.height > cur[1] > boats[j].y:
                        k = 7
                        for i in range(6):
                            if mc[i].pos == boats[j].pos:
                                k = i
                        if k != 7:
                            boats[j].highlight(x,y,mc[k].char)
                            if pygame.mouse.get_pressed() == (1, 0, 0):
                                if mc[k].char=='M':
                                    a -= 1
                                elif mc[k].char == 'C':
                                    b -= 1
                                if mc[k].leftright=='left':
                                    mc[k].x, mc[k].y = mc[k].rect_x - 12, mc[k].rect_y
                                    mc[k].pos = 0
                                elif mc[k].leftright=='right':
                                    mc[k].x, mc[k].y = mc[k].rect_x - 12, mc[k].rect_y
                                    mc[k].pos = 1
                                if boats[j].pos==2 or boats[j].pos==3:
                                    left = False
                                elif boats[j].pos==4 or boats[j].pos==5:
                                    right = False

            #update boat position for movement
            x = x + x_change

            #update missionary and cannibal position for movement
            for i in range(6):
                mc[i].x += mc[i].x_change
            action = [a, b]

        #actions for gameover
        elif gameover and not gameoverplayed:
            pygame.mixer.music.stop()
            losesnd.play(0)
            pygame.time.delay(3000)
            diesnd.play(0)
            gameoverplayed=True

        #actions for game won
        elif won and not wonplayed:
            pygame.mixer.music.stop()
            winsnd.play(0)
            wonplayed = True

        pygame.display.update()
        clock.tick(25)

    pygame.quit()
    quit()

if __name__=="__main__":
    main()