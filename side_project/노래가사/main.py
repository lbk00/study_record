import pygame
import music_lyrics as ml
import sys

global i

pygame.init()
click_flag = 1 #재생 & 정지 판단해주는 플래그
#화면
size = [500,650]
scr = pygame.display.set_mode(size)
scr.fill((150,150,150))
# 노래


pygame.mixer.music.load("YOUNHA.ogg")
pygame.mixer.music.set_volume(2)
pygame.mixer.music.play()



#텍스트
font = pygame.font.SysFont("malgungothic",26,False,True)
#title = font.render(ml.lyrics[1],True, (0 ,0, 0))

#이미지
img = pygame.image.load("D:\Dev\IDE\music_lyrics\윤하.jpg")
img = pygame.transform.scale(img,(300,300))

#도형


while True:
    time_line_ms = pygame.mixer.music.get_pos()
    time_line = time_line_ms//1000# ms -> 초로 변환

    #scr.blit(title,(100,100))

    #이미지
    scr.blit(img,(100,30))

    #시간
    t = ml.show_lyrics(time_line) 

    #재생/멈춤
    if click_flag == 1:
        pygame.draw.polygon(scr,(255,255,255),[[240,540],[240,560],[260,550]])
    else :
        pygame.draw.rect(scr,(255,255,255),[240,540,20,20],10)
    #도형
    pygame.draw.circle(scr,(255,255,255),[100+time_line,510],5)
    pygame.draw.line(scr,(0 ,50, 250),[90,510],[100+time_line,510],3) # 노래 지나간 부분
    pygame.draw.line(scr,(255,255,255),[95+time_line,510],[410,510],3) 

    ly = font.render(ml.lyrics[t],True, (0 ,50, 250))
    if t==56 :  pass
    else : ly_down = font.render(ml.lyrics[t+1],True, (0,0,0))
    #위 아래로 이전가사 이후가사 보여줘도 좋을듯?

    scr.blit(ly,(90,380))
    if t==56 :  pass
    else :  scr.blit(ly_down,(90,430))
    if ml.flag == 1 : scr.fill((150,150,150))
    pygame.display.update()

    scr.fill((150,150,150))
    
    x,y = pygame.mouse.get_pos()# 마우스 위치
    
    pygame.MOUSEMOTION
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if click_flag == 1 and 240 <= x <= 260 and 540 <= y <= 560:
                pygame.mixer.music.pause()
                click_flag = 0
            elif click_flag == 0 and 240 <= x <= 260 and 540 <= y <= 560:
                pygame.mixer.music.unpause()
                click_flag = 1
            

pygame.quit()




