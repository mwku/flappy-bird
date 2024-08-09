import pygame as pg
from config import *
from helper import image_loader

from base import Base
from bird import Bird
from pipe import Pipes
from scoreboard import Scoreboard
import changespeed


class Game:
    """
    遊戲控制物件

    Attributes:
        screen (pg.Surface): 視窗物件
        background_image (pg.Surface): 背景圖片物件
    Methods:
        run(): 開始遊戲(進入遊戲迴圈)
    """

    def __init__(self, surface: pg.surface):
        """
        初始化函式

        Args:
            surface (pg.surface): 視窗物件
        """
        self.screen = surface
        self.background_image = image_loader(
            BACKGROUND_IMG_PATH, (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        self.over_image=image_loader(
            './img/gameover.png',(192,42)
        )
        self.stop=image_loader(
            './img/stop.jpg',(57,55)
        )
        self.start=image_loader(
            './img/start.jpg',(57,55)
        )
        self.speed=image_loader(
            './img/speed.jpg',(100,50)
        )
        self.float=image_loader(
            './img/小數點.jpg',(31,40)
        )
    def start_get_input(self) -> bool:  # 回傳滑鼠是否按下(True: 按下/False: 沒有按下)
        if pg.mouse.get_pressed()[0]:
            return True
        return False
    def space_click(self) ->bool:#回傳空白是否被按下
        if pg.key.get_pressed()[pg.K_SPACE]:
            return True
        return False
    # TODO7 讓遊戲流程更豐富
    def run(self):
        qut=True
        over=False
        start='start'
        hightest_point=0
        while qut:
            clock = pg.time.Clock()
            base = pg.sprite.GroupSingle(Base())
            bird = pg.sprite.GroupSingle(Bird((SCREEN_WIDTH / 10, HEIGHT_LIMIT / 2)))
            pipes = Pipes()
            scoreboard = Scoreboard(history=hightest_point)
                    # game loop
            click=False
            running = True
            click_space=False
            
            while running:
                clock.tick(FPS)                
                for event in pg.event.get():
                    if event.type == pg.QUIT:  # "視窗關閉"事件
                        running = False
                        qut=False           
                            # 更新遊戲
                if self.space_click():
                    start='stop'
                else:
                    start='start'
                if click:
                    if start=='start':#暫停功能(按下滑鼠後按住SPACE可以暫停，SPACE放開後會繼續)
                        over=False
                        base.update(score=pipes.pipes_counter-1)
                        bird.update()
                        pipes.update(update_=True,score=pipes.pipes_counter-1)
                        scoreboard.update(pipes_count=pipes.pipes_counter,history=hightest_point)
                            ## 遊戲結束與否
                            ### 碰撞發生
                                    
                if pg.sprite.groupcollide(bird, pipes.pipes, False, False) and start=='start':
                    running = False
                    over=True
                    
                            # 畫背景、物件
                if over:
                    self.screen.blit(self.over_image,(114,256))
                else:
                    self.screen.blit(self.background_image, (0, 0))
                    bird.draw(self.screen)
                    pipes.draw(self.screen)
                    base.draw(self.screen)
                    scoreboard.draw(self.screen)
                    self.screen.blit(self.float,(140,720))#TODO9隨分數加速(傳遞分數給需要用到BASE_SCROLLING_SPEED的function) 
                    if start=='start':
                        self.screen.blit(self.stop,(0,0))
                    else:
                        self.screen.blit(self.start,(0,0))
                        #歷史紀錄
                    self.screen.blit(self.speed,(0,700))
                    if pipes.pipes_counter-1>hightest_point:
                        hightest_point=pipes.pipes_counter-1
                pg.display.update()
                if self.start_get_input():
                    click=True