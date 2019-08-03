# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 04:35:10 2019

@author: A_Normal_PC
"""

from graphics import *
from classes import *
from functions import *

Y_start=100
X_check_center=75
size=30
gap=13
price_text_offset=120

win = GraphWin("Checklist", 680, 800)

price_text= Text(Point(X_check_center+price_text_offset,Y_start-gap*3),"საბოლოო ფასი:")
price_text.setSize(size)
price_text.draw(win)


full_price= Text(Point(X_check_center+price_text_offset+270,Y_start-gap*3),"0")
full_price.setSize(size)
full_price.draw(win)

checklist=Checklist(win, 'assets/base.xlsx', X_check_center, size, Y_start, gap)

break_condition_met=False

while not break_condition_met:
    clickPoint=win.getMouse()
    
    if clickPoint is not None:
        for button in checklist.check_list:
            if inside(clickPoint, button.rectangle):
                click_val=button.click(win)
                if click_val!=-1:
                    full_price.setText( str(float(full_price.getText())+click_val) )
                else:
                    checklist.undraw_list()
                    checklist.draw_checkout()
                    print("change_mode")
                
win.close()