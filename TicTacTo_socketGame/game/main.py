import pygame
import random
import sys
import numpy as np

O = pygame.image.load("image/O.png")
O = pygame.transform.scale(O,(180,180))
X = pygame.image.load("image/X.png")
X = pygame.transform.scale(X,(180,180))
# 화면설정
def init():
    global rect1,rect2,rect3,rect4,rect5,rect6,rect7,rect8,rect9,rec_pos
    # 보드 배경
    board = Button(screen,300,150,600,600,BOARD,shape='rect')
    # 보드
    rect1 = Button(screen, 300, 150, 200, 200,line=10, color=BOARD_RECT, shape='rect')
    rect2 = Button(screen, 500, 150, 200, 200,line=10, color=BOARD_RECT, shape='rect')
    rect3 = Button(screen, 700, 150, 200, 200,line=10, color=BOARD_RECT, shape='rect')
    rect4 = Button(screen, 300, 350, 200, 200,line=10, color=BOARD_RECT, shape='rect')
    rect5 = Button(screen, 500, 350, 200, 200,line=10, color=BOARD_RECT, shape='rect')
    rect6 = Button(screen, 700, 350, 200, 200,line=10, color=BOARD_RECT, shape='rect')
    rect7 = Button(screen, 300, 550, 200, 200,line=10, color=BOARD_RECT, shape='rect')
    rect8 = Button(screen, 500, 550, 200, 200,line=10, color=BOARD_RECT, shape='rect')
    rect9 = Button(screen, 700, 550, 200, 200,line=10, color=BOARD_RECT, shape='rect')
    # 보드 인덱스 위치
    rec_li = [[[rect1.x+10,rect1.y+10],[rect2.x+10,rect2.y+10],[rect3.x+10,rect3.y+10]],
              [[rect4.x+10,rect4.y+10],[rect5.x+10,rect5.y+10],[rect6.x+10,rect6.y+10]],
              [[rect7.x+10,rect7.y+10],[rect8.x+10,rect8.y+10],[rect9.x+10,rect9.y+10]]]
    # 넘파이로 변환
    rec_pos = np.array(rec_li)

# 버튼 클래스
class Button(object):
    #                   화면,x축,y축,너비,높이,색상,선(기본값 채움),모양(기본값 사각형)
    def __init__(self,display,x,y,width,height,color,line=0,shape = 'rect'):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.line = line
        self.shape = shape
        self.draw()

    # 화면에 표시
    def draw(self):
        if self.shape == 'rect':
            pygame.draw.rect(self.display,self.color,(self.x,self.y,self.width,self.height),self.line)
        elif self.shape == 'circle':
            pass

# 클릭 되었는지 확인
def isClick(button,m_pos):
    x,y,w,h = button.x, button.y,button.width,button.height
    mx = m_pos[0]
    my = m_pos[1]
    # 마우스 좌표가 버튼안에 있을경우 True 리턴
    if x<=mx<=x+w and y<=my<=y+h:
        return True
    else:
        return False

# 선택한 위치 행렬에 표시
def BoardMark(index,user):
    if user == 'O':
        board_matrix[index]=1
    else:
        board_matrix[index]=2

# 보드판에 그림 그림
def BoardDraw(index,user):

    if user == 'O':
        screen.blit(O,index)
    else:
        screen.blit(X,index)

# 유저 턴 바꿔줌
def userTurn(u):
    if u=='O':
        return 'X'
    else:
        return 'O'

# 선택한 위치가 비어있는지 확인
def isBlank(index,u):
    global user
    if board_matrix[index]==0:
        BoardMark(index, u)
        user = userTurn(user)
    else:
        print("여기에 둘수 없습니다.")


if __name__ == "__main__":
    pygame.init()
    # screen
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 900

    # color
    BACKGROUND = (255, 248, 231)
    BOARD = (250, 128, 114)
    BOARD_RECT = (94, 119, 249)

    board_matrix = np.zeros([3,3])
    print(board_matrix)
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    user='O'
    while True:
        # mouse pos
        mousePos = pygame.mouse.get_pos()

        screen.fill(BACKGROUND)
        init()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if isClick(rect1,mousePos):
                    isBlank((0,0),user)


                elif isClick(rect2,mousePos):
                    isBlank((0, 1), user)

                elif isClick(rect3,mousePos):
                    isBlank((0, 2), user)

                elif isClick(rect4,mousePos):
                    isBlank((1, 0), user)

                elif isClick(rect5,mousePos):
                    isBlank((1, 1), user)

                elif isClick(rect6,mousePos):
                    isBlank((1, 2), user)

                elif isClick(rect7,mousePos):
                    isBlank((2, 0), user)

                elif isClick(rect8,mousePos):
                    isBlank((2, 1), user)

                elif isClick(rect9,mousePos):
                    isBlank((2, 2),user)
         
            if event.type in [pygame.K_ESCAPE,pygame.QUIT]:
                pygame.quit()
                sys.exit()
        for i,row in enumerate(board_matrix):
            for j,col in enumerate(board_matrix[i]):
                if board_matrix[i,j]==1:
                    BoardDraw(rec_pos[i,j],'O')
                elif board_matrix[i, j]==2:
                    BoardDraw(rec_pos[i, j],'X')

        pygame.display.flip()
