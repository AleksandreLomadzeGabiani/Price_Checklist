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

background= Image(Point(340,400),"assets/background.png")
background.draw(win)

price_text= Text(Point(X_check_center+price_text_offset,Y_start-gap*3),"საბოლოო ფასი:")
price_text.setSize(size)
price_text.setFill("Yellow")
price_text.draw(win)


full_price= Text(Point(X_check_center+price_text_offset+270,Y_start-gap*3),"0")
full_price.setSize(size)
full_price.setFill("Yellow")
full_price.draw(win)

checklist=Checklist(win, 'assets/base.xlsx', X_check_center, size, Y_start, gap)

break_condition_met=False

finalization_mode=False

while not break_condition_met:
    clickPoint=win.getMouse()
    
    if clickPoint is not None:
        for button in checklist.check_list:
            if inside(clickPoint, button.rectangle):
                click_val=button.click(win)
                if click_val!=None:
                    if click_val!=-1:
                        full_price.setText( str(float(full_price.getText())+click_val) )
                    else:
                        if not finalization_mode:
                            checklist.undraw_list()
                            checklist.draw_checkout()
                            finalization_mode=True
                            print("changed_mode")
                        else:
                            if button.name=="შეკვეთის განთავსება":
                                print("email sent")
                                send_email("""\
Subject: ახალი შეკვეთა \n
                                
                                \n ტელეფონის ნომერი: {}
                                \n საბოლოო ფასი: {}
                                \n შეკვეთის დეტალები: {}""".format(checklist.checkout[-2].getText(), full_price.getText(), checklist.getCheckoutText() ).encode("utf8") )  
                                
                                recieved_order_text_point=checklist.check_list[-1].rectangle.getCenter()
                                
                                for a in range(2):
                                    checklist.check_list[-1].undraw_check()
                                    checklist.check_list=checklist.check_list[:-1]
                
                                for a in range(2):
                                    checklist.checkout[-1].undraw()
                                    checklist.checkout=checklist.checkout[:-1]
                                    
                                recieved_order_text= Text(recieved_order_text_point,"შეკვეთა მიღებულია")
                                recieved_order_text.setSize(30)
                                recieved_order_text.setFill("Green")
                                recieved_order_text.draw(win)
                            else:
                                checklist.undraw_checkout()
                                checklist.draw_list()
                                finalization_mode=False
                                print("changed_mode")
                
win.close()