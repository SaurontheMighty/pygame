#SaurontheMighty
#The Most Amazing Game Ever

import pygame, random, sys

pygame.init()
pygame.mixer.init()

#Initializing screen
size=(900,700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("TMAGE")


#All sprites drawn by Ashish on piskelapp.com
fireball = pygame.image.load("fireball.png")
fireball2 = pygame.image.load("fireball2.png")
fireballimg=fireball



#backgrounds
background1 = pygame.image.load("bg1.png")
endground=pygame.image.load("bg6.png")
background=background1#To change backgrounds easily


#Other images
obstacle = pygame.image.load("obstacle.png")
boost = pygame.image.load("boost.png")
tbutton = pygame.image.load("button.png")#try again
pausebutton2 = pygame.image.load("pause.png")
pausebutton = pygame.image.load("pause_g.png")
slomo = pygame.image.load("slomo.png")


#LEVEL 2
eviloct=pygame.image.load("eviloctopus.png")
portal= pygame.image.load("portal.png")
inkball= pygame.image.load("inkball.png")
fcharge= pygame.image.load("fcharge.png")
hcharge= pygame.image.load("hcharge.png")
zcharge= pygame.image.load("zcharge.png")
fhealth= pygame.image.load("fhealth.png")
hhealth= pygame.image.load("hhealth.png")
zhealth= pygame.image.load("zhealth.png")#z for zero
fehealth= pygame.image.load("fehealth.png")#f for full
tehealth= pygame.image.load("tehealth.png")#t for three fourths
hehealth= pygame.image.load("hehealth.png")#h for half
qehealth= pygame.image.load("qehealth.png")
blast= pygame.image.load("fireblast.png")
sound = pygame.image.load("sound.png")
mute = pygame.image.load("mute.png")



#To change images based on value instead of loading a new image
health=fhealth
charge=fcharge
ehealthbox=fehealth


#Initializing variables
#Player
m_x = 0
m_y = 0

#Obstacle
obx=800
oby=500

#+10 boost
px=790
py=600

#Velocity of obstacle
vob=8

#Velocity of slomo
vslo=9

#Slomo
sx=700
sy=600

#Score
score=0

#Evil Octopus and inkballs
ey=500
ix=773
iy=ey+105
ix2=773
iy2=ey+105
ix3=773
iy3=ey+105

#Health and Charge
healthval=100
chargeval=100

#Health of boss
edeath=False
ehealth=100#octopus health

#Foreground and background for Game Over Text
REDF = (24,255,133)
REDB = (24,255,133)

#Finds previous high score and closes the file so that it can be reopened to write in a new high score(if achieved)
highscores = open("highscores.txt","r")
highscore=highscores.readline()
highscore=highscore.rstrip("\n")
print("Current High Score: ",highscore)
highscores.close()



#Initializing Smoooth controls    
pressed_left=False
pressed_right=False
pressed_up=False
pressed_down=False

#Becomes YOU WON when player wins
x='GAME OVER'


#initializing various boolean values
lost=False#Stops game
pause=False
stop_pause=False#Prevents the player from unpausing when dead and hides pause button
slo=False#To slow down time
nhs=False#Becomes true if the player hits a new high score
notdone = True#Counter for while loop
done_music=False#Music after the player has lost
muted=False


level2=False
l2music=False
portal_collide=False
yreach=False# So that evil octopus can move up and down
attac=False# In level2 when player attacks with (x)
lost2=False

#USEREVENT+1 occurs after every second
pygame.time.set_timer(pygame.USEREVENT+1,1000)#Score Count



#whitenoise.mp3 created on garageband app,
#collision.wav taken from: https://freesound.org/people/kirbydx/sounds/175409/
#youwon.wav taken from: http://soundbible.com/478-Cheering-3.html
#level2.mp3 is a small part of Tchaikovsky's 1812 Overture, a version of which was downloaded from:https://archive.org/details/TCHAIKOVSKY1812Overture-Rodzinski-NEWTRANSFER
music_list=["whitenoise.mp3","collision.wav","nhs.mp3","youwon.mp3","level2.mp3"]#list with all game music
#Code such as music.load and music.play() was adapted from: https://nerdparadise.com/programming/pygame/part3




def music(i,x):#Function that plays music from the list
        if(muted==False):
                pygame.mixer.music.load(music_list[i])
                pygame.mixer.music.play(x)


def obstaclepos(m_x,m_y):#Calculates obstacle position
        if(m_x<400 and m_x>100):#so that obstacle doesn't spawn too close
            temp=m_x+500
        elif(m_x<=100):#Put in because the obstacle was spawning way too close after try again
                temp = m_x+700
        else:
            temp=900
        obx = random.randint(temp, 900)
        oby = random.randint(m_y-100,m_y+100)#very close to obstacle's y coordinate
        return obx,oby





music(0,-1)#Starts music initially
clock = pygame.time.Clock()


while notdone:
        
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                notdone = False#Exit loop if user closes window    
        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                #Try again button
                if ((mouse_pos[0] in range(380,508)) and (mouse_pos[1] in range(650,694)) and lost ==True):
                    music(0,-1)#Restarts music
                    REDF = (24,255,133)
                    lost=False
                    done_music=False
                    score=0
                    px=790
                    py=600
                    stop_pause=False
                    if(lost2==True):#If player dies in level 2
                        #Resets all values
                        REDF = (246,0,0)
                        REDB = (246,0,0)
                        background=endground
                        portal_collide=True
                        px=1000
                        py=1000
                        m_x=100
                        m_y=500
                        lost2=False
                        healthval=100
                        chargeval=100
                        edeath=False
                        ehealth=100#octopus health
                        score=101
                        health=fhealth
                        charge=fcharge
                        ehealthbox=fehealth
                        l2music=False
                        ix2=-200

                
                    if(nhs==True):
                        print("New High Score! "+highscore)
                        nhs=False

                    #Position where player last died
                    if(dieposx!=0 and dieposy!=0):
                        m_x=0
                        m_y=0
                        
                #Quit button 
                if ((mouse_pos[0] in range(460-64,460+64)) and (mouse_pos[1] in range(500-28,500+28)) and lost ==True):
                    notdone=False

                #Pause button 
                if ((mouse_pos[0] in range(0,108)) and (mouse_pos[1] in range(600,648)) and stop_pause==False):
                    if(pause==False):
                            pause=True
                            lost=True
                    else:
                            pause=False
                            lost=False
                            
                if ((mouse_pos[0] in range(0,50)) and (mouse_pos[1] in range(650,700))):
                        if(muted==False):
                                muted=True
                                pygame.mixer.music.pause()
                        else:
                                muted=False
                                done_music=False

                                #Play music based on progress in the game
                                if(level2==False):
                                        music(0,-1)
                                if(lost==True and pause==False):
                                        music(1,0)
                                if(x=='YOU WON'):
                                        music(3,0)
                                if(nhs==True):
                                        music(2,0)     
                                if(level2==True):
                                        music(4,-1)

                            
        elif event.type == pygame.USEREVENT+1:
                if(lost==False):
                    score=score+1#every second score increments

        elif event.type == pygame.KEYDOWN:                    
            if event.key == pygame.K_LEFT:        
                pressed_left = True
            elif event.key == pygame.K_RIGHT:     
                pressed_right = True
            elif event.key == pygame.K_UP:        
                pressed_up = True
            elif event.key == pygame.K_DOWN:     
                pressed_down = True
            elif event.key == pygame.K_f and pause==False and level2==False:#Allows you to skip ahead
                score=35
            elif event.key == pygame.K_s and pause==False and level2==False:#Allows you to skip to the second part of the game
                score=100
            elif event.key == pygame.K_x and level2==True and pause==False and chargeval==100:#player attack
                attac=True
                score_init=score
            elif event.key == pygame.K_SPACE and stop_pause==False:#spacebar to pause
                if(pause==False):
                        pause=True
                        lost=True
                else:
                        pause=False
                        lost=False


        #once key is let go character should stop moving
        elif event.type == pygame.KEYUP:            
            if event.key == pygame.K_LEFT:        
                pressed_left = False
            elif event.key == pygame.K_RIGHT:     
                pressed_right = False
            elif event.key == pygame.K_UP:        
                pressed_up = False
            elif event.key == pygame.K_DOWN:     
                pressed_down = False



#gives character a velocity
    if(lost==False):        
        if pressed_left:
            m_x -= 5
        if pressed_right:
            m_x += 5
        if pressed_up:
            m_y -= 5
        if pressed_down:
            m_y += 5


    #END Screen
    #Text learnt from https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
    font = pygame.font.Font('freesansbold.ttf', 60)
    end_screen = font.render(x, True, REDF, REDB)
    textRect = end_screen.get_rect()
    textRect.center=(450,300)
    screen.blit(end_screen, textRect)



    font1 = pygame.font.Font('freesansbold.ttf', 30)
    #score display
    if(level2==True):
            scoretext = font1.render('Score: '+'infinity', True, (0,0,0), (246,0,0))
    else:
            scoretext = font1.render('Score: '+str(score), True, (0,0,0), (24,255,133))
    scoreRect = scoretext.get_rect()



    #boost(the +10 arrow thing)
    if(lost==False and level2==False):
            screen.blit(boost, (px, py))#Don't blit if the player has lost or paused the game
    if(level2==True and portal_collide==False and stop_pause==False):
            screen.blit(portal,(600,300))


#displays score and fireball
    screen.blit(fireballimg, (m_x, m_y))                
    screen.blit(scoretext, scoreRect)


#displays obstacle if level 2 is not yet reached
    if(stop_pause==False and level2==False):#So that player can still see obstacle when paused
        screen.blit(obstacle, (obx, oby))
        if(lost==False):
                obx-=vob#Speed of obstacle
                if(obx<-110):
                    obx,oby=obstaclepos(m_x,m_y)#calls function


#If player collides with the obstacle
    if(((abs(abs(obx+54)-abs(m_x+54)))<(108)) and (abs(abs(oby+90)-abs(m_y+45))<(135)) and (lost2==False and score<100) or lost2==True):#The score<100 clause is so that when you skip to score 100 an obstacle wont kill you
        #all collisions are just simple applications of coordinate geometry as I was not too keen on classes
        lost=True
        stop_pause=True
        dieposx=m_x#Position where the character last died
        dieposy=m_y
        obx=-110#So that the obstacle does not continue from its last position when you play again
        if(pause==False):
                m_x=380
                m_y=350
                REDF=(0,0,0)
                if(level2==False):
                        REDB = (24,255,133)
                elif(level2==True):
                        REDB = (246,0,0)


#Lost sequence
    if(lost==True and pause==False):

        if(score>int(highscore) and level2==False):#Check for high score
                nhs=True
                newhighscore = open("highscores.txt","w")
                newhighscore.write(str(score))
                highscore=str(score)#writes the new highsore to the txt file 
                newhighscore.close()

                
        font1 = pygame.font.Font('freesansbold.ttf', 30)
        if(level2==True):
                quittext = font1.render(' QUIT ', True, (246,0,0), (0,0,0))#To set the background color appropriately
        else:
                quittext = font1.render(' QUIT ', True, (24,255,133), (0,0,0))
        quitRect = scoretext.get_rect()



        #centers based on level
        if(lost2==True):
                quitRect.center=(490,500)
        else:
                quitRect.center=(450,500)

                
        #Displays quit button and try again button when game is over
        screen.blit(quittext, quitRect)
        if(x!='YOU WON'):#If the person has won, don't show try again
                screen.blit(tbutton, (380, 650))
                

#displays pause button
    if(stop_pause==False and level2==False):
        screen.blit(pausebutton,(0,600))
    elif(stop_pause==False and level2==True):
        screen.blit(pausebutton2,(0,600))


    #Screen loops so that player cannot travel (too much)outside
    if(m_y>630):
        m_y=630
    elif(m_y<-30):
        m_y=-30
    if(m_x>880):
        m_x=860
    elif(m_x<0):
        m_x=0
        

#Increases difficulty over time
    if(score>30 and pause==False):
        obx-=(2*((score-30)/10))#Increases speed of obstacle


#Spawns snail/turtle if score is greater than 40
    if(score>40 and lost==False and level2==False):
            sx-=vslo
            screen.blit(slomo, (sx,sy))

            if(sx<-3000):
                    sx=1000
            if(m_x+108 in range(sx,sx+128) and m_y+45 in range(sy-45,sy+100)):
                    slo = True
                    sx=-10

#If player collides with snail/turtle on rocket, slow down obstacles
    if(slo==True):
            vob=2
            init_score=score
            if(((score-init_score)>4) or stop_pause==True):#Slow will last 4s
                    slo=False
                    vob=8

#Location of the +10 boost after player collides
    if((m_x+108 in range(px,px+128) and m_y+45 in range(py,py+128+45)) and level2==False):
            score=score+10
            m_x=abs(px-790)
            m_y=py
            py=abs(py-600)#Flip flops between top and bottom
            obx=910#Prevents a type of collision that happens after respawn Fix1


#Prints new high score to screen
    if(nhs==True and level2==False):
                font2 = pygame.font.Font('freesansbold.ttf', 30)
                ntext = font2.render(' New High Score! ', True, (10,0,0), (24,255,133))
                nRect = scoretext.get_rect()
                nRect.center=(405,50)
                screen.blit(ntext, nRect)

#Music after you win or game is over
    if(stop_pause==True and done_music==False):
            if(nhs==True):
                music(2,0)
                done_music=True
            elif(x=='YOU WON'):
                music(3,0)
                done_music=True
            else:
                music(1,0)
                done_music=True


    if(muted==False):#Displays speaker icon
            screen.blit(sound, (0,650))
    else:
            screen.blit(mute, (0,650))


#Level 2 code
    if(score>100 and stop_pause==False):
        level2=True
        
        if(l2music==False):#If we don't have this kind of thing then it restarts the music everytime it passes
                music(4,-1)
                l2music=True

        
        if((m_x+108 in range(600,600+150+108)) and (m_y+90 in range(300,600+90)) and portal_collide==False):#if player collides with door, the player has dimensions of 108*90 and the door has 150*300
                portal_collide=True
                px=1000
                py=1000
                m_x=100
                m_y=500
                REDF = (246,0,0)
                REDB = (246,0,0)

        if(portal_collide==True):
                screen.blit(charge,(0,115))#blitting stats
                screen.blit(health,(0,50))
                fireballimg=fireball2
                background = endground
                
                if(edeath==False):#edeath is death of octopus
                        #displays all the level 2 characters
                        screen.blit(eviloct, (700,ey))
                        screen.blit(ehealthbox, (780,ey-10))
                        screen.blit(inkball,(ix,iy))
                        screen.blit(inkball,(ix2,iy2))
                
                if(pause==False):
                        if(ey<=100):
                                yreach=True#Now ey will increase because the octo reached the topmost position
                        elif(ey>=480):
                                yreach=False#Ey will decrease because the lowermost position was reached
                        if(yreach==True):
                                ey+=3
                        elif(yreach==False):
                                ey-=3
                        
                        screen.blit(inkball,(ix3,iy3))#Hides the fast inkball when paused, the rest are displayed outside the pause==False loop
                        ix-=6
                        if(ix<-100):
                                ix=773
                                iy=ey+70
                        ix2-=4
                        if(ix2<-500):
                                ix2 = 600
                                iy2 = m_y
                        elif(ix2>1000 and ix2<1500):
                                ix2=600
                                iy2=m_y
                        ix3-=10
                        if(ix3<-100):
                                ix3=773
                                iy3=ey+70

                #Collisions with either inkballs or octopus should lower player health
                if(abs(m_x-ix)<=108 and abs(m_y-iy)<=90 and edeath==False):
                        healthval=healthval-30
                        ix=-100

                if(abs(m_x-ix2)<=108 and abs(m_y-iy2)<=90 and edeath==False):
                        healthval=healthval-25
                        ix2=2000

                if(abs(m_x-ix3)<=108 and abs(m_y-iy3)<=90 and edeath==False):
                        healthval=healthval-15
                        ix3=-100
                        
                if(m_x+54 in range(700,940) and m_y+45 in range(ey,ey+240) and edeath==False):
                        healthval=healthval-50
                #Changes player's health image accordingly
                if(healthval<=0):
                        lost2=True
                elif(healthval<=25):
                        health=zhealth
                elif(healthval<=50 and healthval>25):
                        health=hhealth
                        
                if(attac==True and stop_pause==False and chargeval==100 and pause==False):
                        fireballimg=blast
                        chargeval=0
                        charge=zcharge
                        attac=False

                        #destroys and respawns inkball if its hit with player's power
                        if(ix in range(m_x,216) and iy in range(m_y,m_y+180)):
                                ix=-10
                                
                        if(ix2 in range(m_x,216) and iy2 in range(m_y,m_y+180)):
                                ix2=2000#remove from screen
                                
                        if(ix3 in range(m_x,216) and iy3 in range(m_y,m_y+180)):
                                ix3=-10
                                
                        if(abs(m_x-700)<216 and abs(m_y-ey)<180):#lowers octo health if player attacks
                                ehealth-=25
                                if(ehealth<=75 and ehealth>50):
                                        ehealthbox=tehealth
                                elif(ehealth<=50 and ehealth>25):
                                        ehealthbox=hehealth
                                elif(ehealth<=25):
                                        ehealthbox=qehealth
                                        
                        if(ehealth==0):#If octopus has zero health
                                edeath=True
                                x='YOU WON'#Changes the game over text to you won text
                                lost2=True
                        if((score-score_init)>=1 or lost2==True):#Just shows the attack image for less than a second
                                fireballimg=fireball2
                                
                #Changes image based the amount of charge
                if(chargeval<100 and pause==False and ((score-score_init)%5==0)):
                        chargeval = chargeval + (score-score_init)/5
                        
                elif(chargeval>100):
                        chargeval=chargeval-(chargeval-100)
                        
                elif(chargeval<=70 and chargeval>=25):
                        charge=hcharge
                        
                elif(chargeval<25 and chargeval>=0):
                        charge=zcharge
                        
                elif(chargeval==100):
                        charge=fcharge
                        
        
    pygame.display.update()
    clock.tick(60)#60 fps

if(nhs==True):
       print("New High Score! ",highscore)
pygame.quit()
