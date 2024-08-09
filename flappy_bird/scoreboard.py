import pygame as pg
from number import Number
import helper
import number
import pygame
from config import *

# TODO6 完成記分板物件
"""
記分板物件需至少支援三個方法
1. __init__(): constructor, 用來建構一個記分板物件實體
2. update(): 用來作為遊戲迴圈中每次更新呼叫的更新函式, 更新記分板物件中的邏輯部分(分數部分)
3. draw(screen): 遊戲迴圈更新後將記分板畫到視窗中的函式
"""

"""
hint: 可以利用實作好的Number物件幫忙
"""


class Scoreboard:
    def __init__(self,history):
        self.Number1=number.Number(position=[224,20],init_value=0)
        self.Number2=number.Number(position=[184,20],init_value=0)
        self.hightest1=number.Number(position=[380,20],init_value=history%10)
        self.hightest2=number.Number(position=[340,20],init_value=history//10)
        self.speed1=number.Number(position=[100,700],init_value=5)
        self.speed2=number.Number(position=[170,700],init_value=0)
    def update(self,pipes_count,history):
        if pipes_count!=1:
            if pipes_count-1//10<1:
                self.Number1.update(pipes_count-1)
            else:
                self.Number1.update((pipes_count-1)%10)
                self.Number2.update((pipes_count-1)//10)
            if history<10:
                self.hightest1.update(history)
            else:
                self.hightest1.update(history%10)
                self.hightest2.update(history//10) 
            if pipes_count-1<20:
                speed=BASE_SCROLLING_SPEED+((pipes_count-1)//5)*0.5
            else:
                speed=BASE_SCROLLING_SPEED+2
            self.speed1.update(int(speed))
            self.speed2.update(int(10*(speed-int(speed))))
            

    def draw(self, screen: pg.Surface):
        self.Number1.draw(screen)
        self.Number2.draw(screen)
        self.hightest1.draw(screen)
        self.hightest2.draw(screen)
        self.speed1.draw(screen)
        self.speed2.draw(screen)
        
