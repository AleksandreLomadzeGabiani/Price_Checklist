# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 07:53:44 2019

@author: A_Normal_PC
"""

from graphics import *
from pandas import *


class Check(object):
    
    def __init__(self, loc, half_size, NAME, PRICE):
        """
        loc is a tuple with x y coordinates of the center of rectangle
        """
        self.disabled=True
        self.clicked=False
        self.name=NAME
        self.price=PRICE
        p1=Point(loc[0]-half_size,loc[1]-half_size)
        p2=Point(loc[0]+half_size,loc[1]+half_size)
        self.rectangle=Rectangle(p1,p2) # x1<x2  y1<y2
        self.rectangle.setFill("white")
        self.name_text=Text(Point(loc[0]+275,loc[1]), NAME)
        self.name_text.setSize(int(half_size*0.9))
        self.name_text.setFill("Yellow")
        self.price_text=Text(Point(loc[0]+525,loc[1]), PRICE)
        self.price_text.setSize(int(half_size))
        self.price_text.setFill("Yellow")
        
    def draw(self,win):
        self.rectangle.draw(win)
        self.name_text.draw(win)
        self.disabled=False
        
        if self.clicked:
            self.price_text.draw(win)
        
    def undraw_check(self):
        self.rectangle.undraw()
        self.name_text.undraw()
        self.disabled=True
        self.price_text.undraw()
    
    def draw_without_rect(self,win):
        self.disabled=True
        self.name_text.draw(win)
        self.price_text.draw(win)
        
    def undraw_without_rect(self):
        self.disabled=True
        self.name_text.undraw()   
        self.price_text.undraw()
        
    def click(self,win):
        if not self.disabled:
            if self.clicked==False:
                self.rectangle.setFill("red")
                self.clicked= not self.clicked
                self.price_text.draw(win)
                return self.price
            else:
                self.rectangle.setFill("white")
                self.clicked= not self.clicked
                self.price_text.undraw()
                return -self.price
        pass
        
class Confirm_check(object):
    
    def __init__(self, loc, half_size, width_mod, length_mod,name, color):
        """
        loc is a tuple with x y coordinates of the center of rectangle
        """
        self.disabled=True
        self.clicked=False
        self.name=name
        self.price=-1
        loc=(340,loc[1])
        p1=Point(loc[0]-half_size*width_mod,loc[1]-half_size*length_mod)
        p2=Point(loc[0]+half_size*width_mod,loc[1]+half_size*length_mod)
        self.rectangle=Rectangle(p1,p2) # x1<x2  y1<y2
        self.rectangle.setFill(color)
        self.name_text=Text(Point(loc[0],loc[1]), self.name)
        self.name_text.setSize(int(half_size*0.75))
        
    def draw(self,win):
        self.rectangle.draw(win)
        self.name_text.draw(win)
        self.disabled=False
    
    def undraw_check(self):
        self.rectangle.undraw()
        self.name_text.undraw()
        self.disabled=True
        
    def click(self,win):
        if not self.disabled:
            self.clicked= not self.clicked
            return self.price  
        
class Checklist(object):
    
    def __init__(self, window, data, X_check_center, check_size, Y_start, gap):
        self.checkout=[]
        self.check_list=[]
        self.data_list=[] # tuples of items (name, price)
        self.win=window
        self.Y_start=Y_start
        self.check_size=check_size
        self.X_check_center=X_check_center
        self.gap=gap
        
        df = pandas.read_excel( data, sheet_name='Sheet1')
        names = df["სამუშაო"]
        prices= df["ფასი"]
        for i in range(len(names)):
                self.data_list.append((names[i],prices[i]))
        
        Y_current=Y_start
        for a in self.data_list:
            print(a)
            self.check_list.append( Check((X_check_center, Y_current+check_size/2), check_size/2, a[0], a[1]) )
            self.check_list[-1].draw(window)
            Y_current+=check_size+gap
            
        self.check_list.append( Confirm_check((X_check_center+200, Y_current+gap*5+check_size/2), check_size*0.75, 5, 1.5,"დადასტურება", "Yellow") )
        self.check_list[-1].draw(window)
        
    def draw_list(self):
        for a in self.check_list:
            a.draw(self.win)
    
    def undraw_list(self):
        for a in self.check_list:
            a.undraw_check()
            
    def getCheckoutText(self):
        text="\n "
        for a in self.checkout[:-2]:
            text+="{} {} \n ".format(a.name,a.price)
            
        return text
    
    def draw_checkout(self):
        self.checkout=[]
        gap=self.gap
        check_size=self.check_size
        X_check_center=self.X_check_center
        Y_current=self.Y_start
        for a in self.check_list[:-1]:
            if a.clicked==True:
                self.checkout.append( Check((-50, Y_current+check_size/2), check_size/2, a.name, a.price) )
                self.checkout[-1].draw_without_rect(self.win)
                Y_current+=check_size+gap
        
        self.checkout.append( Entry( Point(X_check_center+260, Y_current+gap*5+check_size/2), 30))
        self.checkout[-1].draw(self.win)
        self.checkout[-1].setFill("White")
        
        self.checkout.append( Text( Point(X_check_center+40, Y_current+gap*5+check_size/2), "ტელეფონის ნომერი:"))
        self.checkout[-1].setSize(int(check_size*0.35))
        self.checkout[-1].setFill("Yellow")
        self.checkout[-1].draw(self.win)
        
        Y_current+=check_size+gap
        self.check_list.append( Confirm_check((X_check_center+200, Y_current+gap*5+check_size/2), check_size*0.75, 5, 1.5, "შეკვეთის განთავსება", "Yellow") )
        self.check_list[-1].draw(self.win)
        
        Y_current+=check_size+gap*5
        self.check_list.append( Confirm_check((X_check_center+200, Y_current+gap*5+check_size/2), check_size*0.75, 5, 1, "დაბრუნება", "Gray") )
        self.check_list[-1].draw(self.win)
        
    def undraw_checkout(self):
        for a in range(2):
            self.check_list[-1].undraw_check()
            self.check_list=self.check_list[:-1]
            
        for a in range(2):
            self.checkout[-1].undraw()
            self.checkout=self.checkout[:-1]
        
        for a in self.checkout:
            a.undraw_without_rect()